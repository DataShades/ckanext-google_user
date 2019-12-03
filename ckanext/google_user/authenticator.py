# encoding: utf-8

import ckan.logic as logic
import ckan.model as model
import logging
import random
import string
import uuid
from ckan.logic.action.create import _get_random_username_from_email
from google.auth.transport import requests
from google.oauth2 import id_token
from repoze.who.interfaces import IAuthenticator
from urlparse import parse_qs
from zope.interface import implements

import ckanext.google_user.helpers as helpers


log = logging.getLogger(__name__)


class GoogleSignInAuthenticator(object):
    implements(IAuthenticator)

    def authenticate(self, environ, identity):
        input = environ["wsgi.input"]

        payload = parse_qs(input.read(1024 * 10), True)
        if "google-sign-in" not in payload:
            return None

        identity = {"token": payload["token"][0]}

        # return 'sergey'
        if "token" not in identity:
            return None
        token = identity["token"]
        try:
            idinfo = id_token.verify_oauth2_token(
                token, requests.Request(), helpers.google_user_client_id()
            )
        except ValueError:
            # Invalid token
            return None

        if idinfo["iss"] not in [
            "accounts.google.com",
            "https://accounts.google.com",
        ]:
            return None

        userid = str(uuid.uuid3(uuid.NAMESPACE_DNS, str(idinfo["sub"])))
        user = model.User.get(userid)

        if user is None:
            user = _create_user(userid, idinfo["name"], idinfo["email"])
        return user.name


def _create_user(id, name, email):
    while True:
        password = "".join(
            random.SystemRandom().choice(
                string.ascii_lowercase + string.ascii_uppercase + string.digits
            )
            for _ in range(12)
        )
        # Occasionally it won't meet the constraints, so check
        errors = {}
        logic.validators.user_password_validator(
            "password", {"password": password}, errors, None
        )
        if not errors:
            break
    user = model.User(
        id=id,
        fullname=name,
        name=_get_random_username_from_email(email),
        email=email,
        password=password,
    )
    model.Session.add(user)
    model.Session.commit()

    return user

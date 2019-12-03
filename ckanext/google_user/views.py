# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Blueprint


google_user = Blueprint("google_user", __name__)


def get_blueprints():
    return [
        google_user,
    ]

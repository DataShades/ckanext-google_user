# -*- coding: utf-8 -*-
import ckan.plugins.toolkit as tk

CONFIG_CLIENT_ID = "ckanext.google_user.client_id"
CONFIG_CLIENT_SECRET = "ckanext.google_user.client_secret"


def get_helpers():
    return {
        "google_user_client_id": google_user_client_id,
        "google_user_client_secret": google_user_client_secret,
    }


def google_user_client_id():
    return tk.config.get(CONFIG_CLIENT_ID)


def google_user_client_secret():
    return tk.config.get(CONFIG_CLIENT_SECRET)

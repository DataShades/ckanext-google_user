# -*- coding: utf-8 -*-

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.exceptions import CkanConfigurationException

import ckanext.google_user.helpers as helpers


class Google_UserPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # ITemplateHelpers

    def get_helpers(self):
        return helpers.get_helpers()

    # IConfigurer

    def update_config(self, config_):
        if toolkit.config.get(helpers.CONFIG_CLIENT_ID) is None:
            raise CkanConfigurationException(
                "Missing Google Client ID: {}".format(helpers.CONFIG_CLIENT_ID)
            )
        if toolkit.config.get(helpers.CONFIG_CLIENT_SECRET) is None:
            raise CkanConfigurationException(
                "Missing Google Client Secret: {}".format(
                    helpers.CONFIG_CLIENT_SECRET
                )
            )

        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("fanstatic", "google_user")

=============
ckanext-google_user
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!


------------
Requirements
------------

.. For example, you might want to mention here which versions of CKAN
    this extension works with.


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-google_user:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-google_user Python package into your virtual environment::

     pip install ckanext-google_user

3. Add ``google_user`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Add ``ckanext.google_user.authenticator:GoogleSignInAuthenticator``
   to ``authenticators`` section of ``who.ini``::

     [authenticators]
      plugins =
       auth_tkt
       ckan.lib.authenticator:UsernamePasswordAuthenticator
       ckanext.google_user.authenticator:GoogleSignInAuthenticator

5. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

Document any optional config settings here. For example::

    # Client Id and secret - [OAuth](https://console.developers.google.com/apis/credentials).
    # (required).
    ckanext.google_user.client_id = 128970851846-otatl76tvrh52fn0r0hi7707225o055j.apps.googleusercontent.com
    ckanext.google_user.client_secret = tLmWfCrUcUvsIY08Gsj0oQn1

------------------------
Development Installation
------------------------

To install ckanext-google_user for development, activate your CKAN virtualenv and
do::

    git clone https://github.com//ckanext-google_user.git
    cd ckanext-google_user
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.google_user --cover-inclusive --cover-erase --cover-tests

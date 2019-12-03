ckan.module("google-sign-in", function($, _) {
  "use strict";
  var auth_ready = $.noop;
  var auth_error = $.noop;
  var _auth2 = new Promise(function(success, error) {
    auth_ready = success;
    auth_error = error;
  });

  return {
    _auth2: _auth2,

    options: {
      clientId: null
    },
    initialize: function() {
      this._token_field = this.el.find("#google-si-token-field");
      window.onGoogleSignIn = this.onGoogleSignIn;
      this._load(this.options.clientId);
      this.el.on("submit", this._onSignIn.bind(this));
    },

    _load: function(id) {
      var self = this;

      window.gapi.load("auth2", function() {
        auth_ready(
          Promise.resolve(
            window.gapi.auth2.init({
              client_id: id,
              fetch_basic_profile: true,
              scope: "profile"
            })
          )
        );
      });
    },

    onGoogleSignIn: console.log,

    _onSignIn: function(e) {
      e.preventDefault();
      this.signIn().then(function() {
        e.target.submit();
      });
    },

    signIn: function() {
      // Sign the user in, and then retrieve their ID.
      var self = this;
      return this._auth2
        .then(function(auth2) {
          return auth2.signIn();
        })
        .then(
          function(user) {
            self._token_field.val(user.getAuthResponse().id_token);
          },
          function(err) {
            console.warn("Google Sign-In: %o", err);
          }
        );
    },
    signOut: function() {
      var auth2 = window.gapi.auth2.getAuthInstance();
      auth2.signOut().then(function() {
        console.log("User signed out.");
      });
    }
  };
});

""" `gae_lib_config` gets loaded in __init__."""
import sys
import os


def load_google_appengine_package():
    """
    In development, we load the google.appengine package so that we can import it anywhere else.

    The full absolute path to local installation of the gcloud sdk should be set in
    'GCLOUD_SDK_PATH'.
    If this value is not found in the environment variables, a RuntimeError is raised
    """
    # if we are not in production, load the google.appengine package from gcloud sdk
    if not os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        gae_package_path = os.getenv('GCLOUD_SDK_PATH')
        if not gae_package_path:
            raise RuntimeError(
                "Environment variable 'GCLOUD_SDK_PATH' must be set to " +
                "the full path of your local installation of gcloud sdk"
            )

        sys.path.insert(
            0,
            os.path.join(
                gae_package_path, os.path.sep.join(['platform', 'google_appengine'])
            )
        )
    print 'google.appengine package has been loaded'

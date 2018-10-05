# gae_env

Console-visible environment variables for Google Appengine projects

#
## Overview

By default, GAE environment variables may be [configured in the app.yaml file][1] or uploaded via a secrets.json.

But, for sensitive data, you should not store it in source code as it will be checked into source control.
Even if you dont, the wrong people (inside your organization) may find it there.

Also, your development environment probably uses different config values from your production environment.
If these values are stored in code, you will have to run different code in development and production, which is not just messy but also bad practice.

# 

`gae_env` reads environment variables from [Cloud Datastore][7] (and/or system environment variables). This way, it becomes more convenient to edit variables in the [Developer's Console][2]

## Usage

```python
# coding: utf-8
import gae_env
from gae_env import ValueNotSetError, NOT_SET_VALUE

key_foo = 'foo'

# get the value stored at key 'key_foo'
value_bar = gae_env.get(key_foo)

# By default, values are of type str

# get value as int
value_bar = gae_env.get(key_foo, converter_class=int)

# get value as float
value_bar = gae_env.get(key_foo, converter_class=float)

# ******************************************************************************
# If there is a value for a key in the system environment variables or datastore,
# it will be returned.
# Else, a place holder record will be created and ValueNotSetError exception will be raised.
# The exception will remind you to go to the Developers Console
# and update the placeholder record.
# ******************************************************************************

# The default error raising behaviour can be turned off with a param
# get value without raising any ValueNotSetError
value_bar = gae_env.get(key_foo, raise_value_not_set_error=False)

# If no value has been set for a key and raise_value_not_set_error=False,
# it will return NOT_SET_VALUE.
# To return None instead, pass return_none_for_not_set_value=True
value_bar = gae_env.get(
    key_foo, raise_value_not_set_error=False, return_none_for_not_set_value=True
)

# There's a convenience method for setting the value of a key at runtime
# NB: This sets the value in Cloud Datastore (not system environment variables)
value_bar = 'bar'
gae_env.set_value(name=key_foo, value=value_bar)

```

**How to set Datastore values in the App Engine console:**

- Go to the [console][2].

- Select your project at the top of the page if it's not already selected.

- In the Kind dropdown box, select GaeEnvSettings.

- Your keys will show up. For those where an exception was raised, they will all have the value `__NOT_SET__`. Click each one and set its value.


## Dependencies

`gae_env` uses the `ndb` library which uses [MemCache][6] and [Cloud Datastore][7] under the hood, so it's fast.

But this also means it requires the context of a Google Appengine runtime in order to work, and can be used in Google Appengine projects only


## Testing
This project uses [`nose`][3], [`nosegae`][4] and [`coverage`][5] for testing. You must have these installed

In addition, you must have gcloud sdk installed, with google appengine enabled.

Run:

    export GAE_LIB_ROOT=/path/to/local/google-cloud-sdk/platform/google_appengine/
    python setup.py nosetests --gae-lib-root=$GAE_LIB_ROOT


## Contributing

1. Fork it (<https://github.com/Odame/gae-env/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request



[1]: https://cloud.google.com/appengine/docs/standard/python3/config/appref#runtime_and_app_elements
[2]: https://console.cloud.google.com/datastore/
[3]: https://nose.readthedocs.io/en/latest/index.html
[4]: https://github.com/Trii/NoseGAE
[5]: https://coverage.readthedocs.io/en/coverage-4.5.1x/
[6]: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjgjpb-ue7dAhVpL8AKHfCBAPAQFjAAegQIChAB&url=https%3A%2F%2Fcloud.google.com%2Fappengine%2Fdocs%2Fstandard%2Fpython%2Fmemcache%2F&usg=AOvVaw1zwnB3ofKYNGfyHRqq_i2j
[7]: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwip1q-Huu7dAhURTsAKHYM3BJcQFjAAegQICBAB&url=https%3A%2F%2Fcloud.google.com%2Fdatastore%2Fdocs%2Fconcepts%2Foverview&usg=AOvVaw0gMRTKGWVdpgoM40VbA9BC
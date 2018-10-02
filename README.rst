If it's sensitive data, you should not store it in source code as it will be checked into source control.
The wrong people (inside or outside your organization) may find it there.
Also, your development environment probably uses different config values from your production environment.
If these values are stored in code, you will have to run different code in development and production, which is not just messy but also bad practice.

Your application would do this to get a value:

API_KEY = Settings.get('API_KEY')
If there is a value for that key in the datastore, you will get it. If there isn't, a placeholder record will be created and an exception will be thrown. The exception will remind you to go to the Developers Console and update the placeholder record.

I find this takes the guessing out of setting config values. If you are unsure of what config values to set, just run the code and it will tell you!

The code above uses the ndb library which uses memcache and the datastore under the hood, so it's fast.

Update:

How to set Datastore values in the App Engine console:

Go to https://console.cloud.google.com/datastore/
Select your project at the top of the page if it's not already selected.
In the Kind dropdown box, select GaeEnvSettings.
If you ran the code above, your keys will show up. They will all have the value __NOT_SET__. Click each one and set its value.


Acknowledgements
NB: The concepts used in this project were inspired by the contributions of other developers on StackOverflow post:
https://stackoverflow.com/questions/22669528/securely-storing-environment-variables-in-gae-with-app-yaml.
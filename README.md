This simple django app generates random UUIDs.
It returns a timestamp as a key and the UUID generated for that timestamp as its value.

REPO NAVIGATION
1. uuid_app/
- contains django default app files (settings.py, urls.py etc)

2. app/
- contains app specific files and folders
- models.py: models (database fields)
- tests.py: models.py tests and views.py tests
- urls.py: url configurations
- views.py: views to display models

3. app/api
- contains app api config
- serializers.py: serializes model output to JSON format
- urls.py: url mapping
- views.py: views to display serialized models

4. app/templates/app
- contains templates rendered by views


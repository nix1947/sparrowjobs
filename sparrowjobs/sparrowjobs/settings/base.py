import json
# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured
# JSON-based secrets module
with open("secrets.json") as f:
secrets = json.loads(f.read())
.
def get_secret(setting, secrets=secrets):
"""Get the secret variable or return explicit exception."""
try:
return secrets[setting]
except KeyError:
error_msg = "Set the {0} environment variable".format(setting)
raise ImproperlyConfigured(error_msg)
SECRET_KEY = get_secret("SECRET_KEY")
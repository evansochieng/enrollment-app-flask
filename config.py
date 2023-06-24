import os

# create Config class
class Config(object):
    # this is the secret key thta heps prevent hackers getting into your application
    SECRET_KY = os.environ.get("SECRET_KEY") or "secret_string"
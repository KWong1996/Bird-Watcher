import json

# Secure Secret Key Logic

# JSON-based secrets module
with open('secrets.json') as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    '''Get the secret variable or return explicit exception.'''
    try:
        return secrets[setting]
    except KeyError:
        print("[ERROR] Missing secrets.json")


consumer_key = get_secret("CONSUMER_KEY")
consumer_secret = get_secret("CONSUMER_SECRET")
access_token = get_secret("ACCESS_TOKEN")
access_token_secret = get_secret("ACCESS_TOKEN_SECRET")


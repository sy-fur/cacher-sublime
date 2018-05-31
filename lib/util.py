import os.path
import json
import yaml

home = os.path.expanduser("~")
cacher_dir = os.path.join(home, ".cacher")
credentials_file = os.path.join(cacher_dir, "credentials.json")


def credentials_exist():
    return os.path.exists(credentials_file)


def get_credentials():
    if credentials_exist():
        with open(credentials_file) as creds_file:
            return json.load(creds_file)
    else:
        return None


def save_credentials(key, token):
    if not os.path.exists(cacher_dir):
        os.mkdir(cacher_dir)

    with open(credentials_file, "w") as file:
        content = {"key": key, "token": token}
        json.dump(content, file)


def load_config():
    file_dir = os.path.dirname(__file__)
    config_file = os.path.join(file_dir, "../", "config.dev.yml")

    with open(config_file, "r") as ymlfile:
        return yaml.load(ymlfile)


def validate_input(expr):
    return len(expr) > 0

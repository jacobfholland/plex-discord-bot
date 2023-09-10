import os

from dotenv import load_dotenv


def load_envs(root_dir='.'):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file == '.env':
                env_file_path = os.path.join(root, file)
                load_dotenv(env_file_path)


load_envs()


class Config:
    APP_NAME = os.environ.get("APP_NAME")
    APP_TIMEZONE = os.environ.get("APP_TIMEZONE")

    LOG_SENSITIVE_DATA = eval(os.environ.get("LOG_SENSITIVE_DATA"))
    LOG_LEVEL = os.environ.get("LOG_LEVEL").upper()
    LOG_PATH = os.environ.get("LOG_PATH")

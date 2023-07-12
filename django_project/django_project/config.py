import os


class AppConfig:
    DEBUG = os.getenv('DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')
    ROOT_URLCONF = os.getenv('ROOT_URLCONF')
    BASE_DIR = os.getenv('BASE_DIR')
    WSGI_APPLICATION = os.getenv('WSGI_APPLICATION')

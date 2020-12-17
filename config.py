import pathlib
import os


BASE_DIR = pathlib.Path(__file__).parent

DOU_GENERAL_URL = 'https://dou.ua/'
LOCALHOST = "http://127.0.0.1:8888/"


class Config:
    DEBUG = True
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'sqlite:///' + str(BASE_DIR/'db.sqlite3')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '(8dvwf@-b62qg(q2xold%yr4%bz-gw9@anm5w39+id_rid2ntg'

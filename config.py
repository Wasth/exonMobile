import os


class Config(object):
    SECRET_KEY = os.environ.get('secret_key') or 'MyMostSecretKey'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'mail.exxonmobile@gmail.com'
    MAIL_PASSWORD = '79eexon1999[]'
    ADMINS = ['mail.exxonmobile@gmail.com']


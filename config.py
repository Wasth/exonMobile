import os


class Config(object):
    SECRET_KEY = os.environ.get('secret_key') or 'MyMostSecretKey'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'mail.exxonmobile@gmail.com'
    MAIL_PASSWORD = '79eexon1999[]'
    ADMINS = ['mail.exxonmobile@gmail.com']
    # RECAPTCHA_PUBLIC_KEY = '6LdME70UAAAAAHlpm3rrGVOdhssvzyUXfvN9lxmw'
    # RECAPTCHA_PRIVATE_KEY = '6LdME70UAAAAAGt26mdNf2rmxy0AZNDSDSo3Ywc4' reCaptcha v3
    RECAPTCHA_PUBLIC_KEY = '6Lf4BL8UAAAAAA7NZoOS8OiAFNUtYxUjOpQBMu3k'
    RECAPTCHA_PRIVATE_KEY = '6Lf4BL8UAAAAAKHnVJszlxnjTRvjCLBwc0ode8EI'
    TESTING = True

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #    'sqlite:///' + os.path.join(basedir, 'app2.db')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@127.0.0.1:3306/kathydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1w2e3r4t5y6u'
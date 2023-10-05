import os
import openai

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'iai.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"


openai.api_key = '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'

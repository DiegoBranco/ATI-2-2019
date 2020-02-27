import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGO_URI = os.environ.get('MONGO_URI') or "mongodb+srv://adrianjmejias:adri_123_123@development-lvhve.mongodb.net/test?retryWrites=true&w=majority"
    LANGUAGES = ['en', 'es']


print(os.environ.get('MONGO_URI'))
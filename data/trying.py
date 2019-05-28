import mongoengine

class Game(mongoengine.Document):
    title = mongoengine.StringField(required=True)
    levels = 
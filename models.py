from peewee import *

db = SqliteDatabase("database.db")

class BaseModel(Model):
    class Meta:
        database = db


# Models go here


class User(BaseModel):
    name = CharField()
    address = CharField()
    payment = IntegerField()


# In order to facilitate search and categorization:
# a product must have a number of descriptive tags
class Tag(BaseModel):
    tag = CharField(unique = True)


class Product(BaseModel):
    name = CharField()
    description = CharField()
    price = FloatField()
    quantity = IntegerField()
    tags = ForeignKeyField(Tag, backref="tags_product")

class UserProduct(BaseModel):
    owner = CharField()
    product = CharField()
    quantity = IntegerField()
    tags = ForeignKeyField(Tag, backref="tags_userproduct")

class OrderTransaction(BaseModel):
    date = CharField()
    user = CharField()
    product = CharField()
    quantity = IntegerField()

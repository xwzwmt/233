from django.db import models
from mongoengine import *
from mongoengine import connect
connect('ershouche',host='127.0.0.1',port=27017)

class Info(Document):
    price=StringField()
    carid=StringField()
    car_type=StringField()
    brand=StringField()
    sys=StringField()
    area=StringField()
    sendtime=StringField()

    meta={'collection':'infoX'}

def data_gen(area):
    pipeline=[
        {'$match':{'area':{'$regex':'上海'}}},
        {'$group':{'_id':'$brand','a':{'$sum':1}}},
        {'$sort':{'a':1}}
    ]

# def data_gen(area):
#     pipeline=[
#         {'$match':{'area':{'$regex':'上海'}}},
#         {'$group':{'_id':'$brand','counts':{'$sum':1}}},
#         {'$sort':{'counts':1}}
#     ]
#     for i in Info._get_collection().aggregate(pipeline):
#         data={
#             'name':i['_id'],
#             'data':[i['counts']],
#             'type':'colum'
#         }
#         yield data

    for i in Info._get_collection().aggregate(pipeline):
        yield [i['_id'],i['a']]


for i in data_gen("上海"):
    print(i)

# Create your models here.

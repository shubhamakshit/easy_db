from Schema import Schema
from DataObject import DataObject
from datetime import datetime
import random
from Database import Database

db = Database('mongodb+srv://admin:admin@opcluster.ka36flg.mongodb.net/?retryWrites=true&w=majority&appName=OPCluster','test','test')

sch = Schema(
    {
        'name':
                {
                    'type': str,
                    "default": "John Doe",
                    "apply": lambda x: x.upper()
                }, 

        'age':  {
                    'type': int,
                    'default': 18,
                    'apply': lambda x: random.randint(18, 60),
                    'required': True
                },

        'email':
                {
                    'type': str,
                    'default': 'akshitshubhammas@gmail.com',
                },

        'posted_at':
                {
                    'type': str,
                    'default': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'apply': lambda x: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
    }
)

for i in range(10):
    db.create(sch,{})

db.printAll()


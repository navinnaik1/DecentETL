from app import db
import time; 

class Coin(db.Model):
    _tablename_ = 'coins'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    indicator1=db.Column(db.String)
    indicator2=db.Column(db.String)
    timestamp=db.Column(db.String,default=round(time.time()))

    def _init_(self, price,indicator1,indicator2):
        self.price = price
        self.indicator1=indicator1
        self.indicator2=indicator2

    def _repr_(self):
        return '<id {}>'.format(self.id)

    
    def serialize(self):
        return {
            'id': self.id, 
            'price': self.price,
            'indicator1':self.indicator1,
            'indicator2':self.indicator2,
            'timestamp':self.timestamp 
        }
from main import db

class Shelter(db.Model):
    __tablename__="shelters"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    phone = db.Column(db.String())
    address = db.Column(db.String())
    city = db.Column(db.String())
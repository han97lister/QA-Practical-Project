from application import db

class Prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket = db.Column(db.String(10), nullable=False)
    prize = db.Column( db.String(255), nullable=False)
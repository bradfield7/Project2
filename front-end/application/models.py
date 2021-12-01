from application import db

class babies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    baby_name = db.Column(db.String(20))
    league_name = db.Column(db.String(30))
    club_name = db.Column(db.String(40))

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class SharkSign(db.Model):
    __tablename__ = 'sharksign'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String)
    active = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)
    events = db.relationship('SharkSignHistory', backref='sharksign',
                             lazy='dynamic')

    def __init__(self, location, active, created_at=None):
        self.location = location
        self.active = active
        if created_at is None:
            self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<SharkSign #{}>'.format(self.id)

class SharkSignHistory(db.Model):
    __tablename__ = 'sharksignhistory'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    sharksign_id = db.Column(db.Integer, db.ForeignKey('sharksign.id'))

    def __init__(self, state, sharksign_id, created_at=None):
        self.state = state
        self.sharksign_id = sharksign_id
        if created_at is None:
            self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<SharkSignHistory #{}>'.format(self.id)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

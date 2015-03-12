from app import db
from sqlalchemy.dialects.postgresql import JSON


class Drug(db.Model):
    __tablename__ = 'drugs'

    id = db.Column(db.Integer, primary_key=True)
    drug_name = db.Column(db.String())
    compound_weight = db.Column(db.String())

    def __init__(self, drug_name, compound_weight):
        self.drug_name = drug_name
        self.compound_weight = compound_weight

    def __repr__(self):
        return '<id {}>'.format(self.id)


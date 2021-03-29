from app import db,ma
import datetime
from sqlalchemy import Column, Integer, DateTime
from marshmallow import Schema, fields
from decimal import Decimal



class Files(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String())
    created_on = db.Column(DateTime, default=datetime.datetime.utcnow)


class Invoice(db.Model):
    __tablename__ = 'invoice'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10,2))
    due_on = db.Column(DateTime)
    sell_price = db.Column(db.Numeric(10,2))


class InvoiceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Invoice
        # fields = ("id", "amount", "due_on","sell_price")
    id = fields.Int()
    amount = fields.Str()
    due_on = fields.Date()
    sell_price = fields.Str()
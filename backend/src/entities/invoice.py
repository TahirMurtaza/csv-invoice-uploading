# coding=utf-8

from marshmallow import Schema, fields
from sqlalchemy import Column, String


# class fileSchema(Schema):
#     id = db.Column(db.Integer, primary_key=True)
#     filename = fields.str()
#     created_at = fields.DateTime()
#     updated_at = fields.DateTime()
    

class InvoiceSchema(Schema):
    id = fields.Number()
    invoice_amount = fields.str()
    invoice_due_on = fields.DateTime()
    
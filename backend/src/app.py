from flask import Flask,render_template, request,abort,jsonify,Response
from flask_sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
import os
import csv
from datetime import date
import datetime
from flask_marshmallow import Marshmallow
import json

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)

from entities.models import Files,Invoice,InvoiceSchema


@app.route('/')
def home():
    return "Backend Running !"


@app.route('/csv_uploader', methods = ['GET', 'POST'])
@cross_origin()
def upload_file():
    try:
        if request.method == 'POST':
            f = request.files['file']
            if f.filename != '':
                file_ext = os.path.splitext(f.filename)[1]
                if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                    abort(400)
                filepath = os.path.join(app.config['UPLOADS_PATH'], f.filename)
                f.save(filepath)
                output = process_csv(filepath)
                return jsonify({"message": "CSV successfully uploaded!","output": output})
    except Exception as e:
        return jsonify({"message": str(e)})



def process_csv(filepath):
    try:
        f = open(filepath)
        csv_f = csv.reader(f)
        invoice_id=0
        amount= 0
        due_on = None
        output = []
        outputmsg=None
        for row in csv_f:
            invoice_id = row[0]
            amount = row[1]
            due_on = row[2]

            # validate each row 
            if(validateInt(invoice_id) and validateAmount(amount) and validateDate(due_on)):
                invoice_id = int(invoice_id)
                amount = float(amount)
                due_on = datetime.datetime.strptime(due_on, '%Y-%m-%d').date()
                today = datetime.datetime.now().date()
                
                # get days between dates
                days = today - due_on
                sell_price = 0

                if days.days > 30:
                    # set coeff 0.5 if greater than 30 days
                    sell_price = 0.5 * amount
                elif days.days <= 30:
                    # set coeff 0.3 if lesser or equal than 30 days
                    sell_price = 0.3 * amount

                # find invoice if exist    
                inv_exist = Invoice.query.filter_by(id=invoice_id).first()
                
                if not inv_exist:
                    #insert if record does not exist
                    inv = Invoice(id=invoice_id,amount=amount,due_on=due_on,sell_price=sell_price)
                    db.session.add(inv)
                    outputmsg = "Invoice Record added Id={}, Amount={}, Due On={},Sell Price={}". format(invoice_id,amount,due_on,sell_price)
                else: 
                    #update if record already exist
                    inv_exist.amount = amount
                    inv_exist.due_on = due_on
                    inv_exist.sell_price = sell_price
                    outputmsg = "Invoice Record updated Id={}, Amount={}, Due On={},Sell Price={}". format(invoice_id,amount,due_on,sell_price)
                db.session.commit()
                output.append(outputmsg)
            else:
                outputmsg = "Invalid data inserted Id={}, Amount={}, Due On={}". format(invoice_id,amount,due_on)
                output.append(outputmsg)
        for txt in output:
            outputmsg += txt + '<br>'

        return outputmsg
        
        #return None
    except Exception as e:
        return str(e)
        



def validateInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def validateDate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        #"Incorrect data format, should be YYYY-MM-DD"
        return False

def validateAmount(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

@cross_origin()
@app.route('/getinvoices',methods=['GET'])
def get_invoice_all():
    invoices = Invoice.query.all()
    invoice_schema = InvoiceSchema(many=True)
    return jsonify(invoice_schema.dump(invoices))




if __name__ == '__main__':
    app.run()
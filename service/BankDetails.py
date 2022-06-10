from sqlalchemy import create_engine, null,update,text
from flask import request,jsonify
from service import connection
from service import apiResponse
from datetime import datetime,date
from models import master

def getAllBankdetails():
    c = connection.connect()
    data = c.execute('select * from bankdetails')
    response = apiResponse.res(data,"Success",200)
    return response

def createBankdetails(data):
    c  =  connection.connect()
    response = jsonify(data)
    data = request.get_json()
    id         = data['id']
    id_temp    =   data['id']
    employeeId = data['employee_id']
    bankName   = data['bank_name']
    bankBranch = data['bank_branch']
    accNo      =  data['acc_no']
    ifscCode   = data['ifsc_code']
    micrCode   =  data['micr_code']
    isActive   = data['is_active']
    createdAt  = str(date.today())
    updatedAt  = str(date.today())
    selectQuery = text("SELECT * from bankdetails where id = %d" % (id))
    ids = c.execute(selectQuery).first()
    if ids is not None:
      query  =  "UPDATE bankdetails set employee_id  =  %d,bank_name  =  '%s', bank_branch  =  '%s', acc_no  =  '%s',ifsc_code =  '%s',micr_code =  '%s',is_active  =  '%s',created_at =  '%s',updated_at = '%s' where id = %d" % (employeeId,bankName,bankBranch,accNo,ifscCode,micrCode,isActive,createdAt,updatedAt,id)
      c.execute(query)
      response = apiResponse.res([data],"Success",200)         
      c.close()
      return response
    else:
        c.execute('INSERT INTO bankdetails(id, employee_id,bank_name,bank_branch,acc_no,ifsc_code,micr_code,is_active,created_at,updated_at) VALUES(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)',
         (id, employeeId,bankName,bankBranch,accNo,ifscCode,micrCode,isActive,createdAt,updatedAt))
        response = apiResponse.res([data],"Success",200)
        c.close()
        return response

def delete(data):
    c  =  connection.connect()
    query = "DELETE from bankdetails where id = %d" % (data)
    c.execute(query)
    response = "deleted successfully"
    c.close()
    return response
   
def masterInsert(data):
    c  =  connection.connect()
    response = jsonify(data)
    data = request.get_json()
    id = data['id']
    shortName = data['shoertName']
    deviceName = data['deviceName']
    isActive = data['isActive']
    c.execute('INSERT INTO master(id, shoertName,deviceName,isActive) VALUES(%s, %s,%s,%s)', (id,shortName,deviceName,isActive))
    response = apiResponse.res([data],"Success",200)
    c.close()
    return response   


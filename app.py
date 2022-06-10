from flask import Flask,request,jsonify
from sqlalchemy import create_engine
from service import BankDetails
from models import master

app=Flask(__name__)




@app.route("/getAllBankdetails", methods=['POST'])
def getAllBankdetails():    
    # data=request.get_json()
    response=BankDetails.getAllBankdetails() 
    return response;

@app.route("/createBankdetails",methods=['POST'])
def createBankdetails():
    data = request.get_json()
    response=BankDetails.createBankdetails(data)
    return response

@app.route("/master",methods=['POST'])
def master():
    data=request.get_json()
    response=BankDetails.masterInsert(data)
    return response   

@app.route("/delete/<int:id>", methods = ["DELETE"])
def delete(id):
    response = BankDetails.delete(id)
    return response     

  
if __name__ == "__main__":
    app.run(debug=True)


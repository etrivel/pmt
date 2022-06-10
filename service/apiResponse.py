from flask import jsonify

def res(data, message, code):
    response = jsonify({'result': [dict(row) for row in data],'message':message,'code':code})
    return response

import os
import flask
from flask import request,jsonify
from scaper import MainClass 





@app.route('/', methods=['GET'])
def VehicalDetails():
    return "Mafiaboy Server"
    


@app.route('/vehical_details/<reg_number>')
def VehicalDetails(reg_number):
    
    registration_number = str(reg_number)
    try:
        m = MainClass()
        data = m.vehicalDetailFromRegNumber(registration_number)
        jsonData = jsonify(data)
        return jsonData
    except KeyError:
        return "invalid input "




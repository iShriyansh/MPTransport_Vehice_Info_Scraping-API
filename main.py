
import os
import flask
from flask import request,jsonify
from scaper import MainClass




app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def VehicalDetailsx():
    return "<h1>Mafiaboy server <h1>"
    


@app.route('/vehical_details/<reg_number>')
def VehicalDetails(reg_number):
    
    registration_number = str(reg_number)
    try:
        m = MainClass()
        data = m.vehicalDetailFromRegNumber(registration_number)
        jsonData = jsonify(data)
        m.driver.quit()
        return jsonData
    except KeyError:
        return "invalid input "
    


@app.route('/license_details')
def license_detail():
    number = request.args.get("reg_number")
    dob = request.args.get("dob")
    try:
        m = MainClass()
        data = m.getDrivingLicenseDetailsByDLNumber(number,dob)
        jsonData = jsonify(data)
        m.driver.quit()
        return jsonData
    except KeyError:
        return "invalid input "



@app.route('/l_license_details/<path:regNumber>/')
def l_license_detail(regNumber):
    try:
        m = MainClass()
        data = m.getLearningLicenseDetailsByDLNumber(regNumber)
        jsonData = jsonify(data)
        m.driver.quit()
        return jsonData
    except KeyError:
        return "invalid input "


@app.route('/bus_tt/<source>/<destination>/')
def bus_time_table(source,destination):
    
    try:
        m = MainClass()
        data = m.getBusesTimeTable(source,destination)
        jsonData = jsonify(data)
        m.driver.quit()
        return jsonData
    except KeyError:
        return "invalid input "



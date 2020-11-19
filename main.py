
import os
import flask
from flask import request,jsonify
from scaper import MainClass 



# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name

# if __name__ == '__main__':
#    app.run(debug = True)





@app.route('/vehical_details/<reg_number>', methods=['GET'])
def VehicalDetails(reg_number):
    
    registration_number = str(reg_number)
    try:
        m = MainClass()
        data = m.vehicalDetailFromRegNumber(registration_number)
        jsonData = jsonify(data)
        return jsonData
    except KeyError:
        return "invalid input "




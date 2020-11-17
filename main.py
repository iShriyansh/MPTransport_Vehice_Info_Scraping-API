from selenium import webdriver
import time
from bs4 import BeautifulSoup
import os

import flask
from flask import request,jsonify


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


def getVehicalDetailJson(mydivs, detail_part):
    detailedVehicalData = {}
    for i in range(len(detail_part)):
        detail_key_id = list(detail_part)[i]
        DetailsRow = mydivs.findAll("fieldset")[detail_key_id].findAll("tr")
        jsonObject = {}
        for i in range(0,len(DetailsRow)):
            rowtd = DetailsRow[i].findAll('td')
            key = rowtd[0].text.strip()
            value = rowtd[2].text.strip()
            jsonObject[key] = value
            if len(rowtd) >4:         
                key = rowtd[4].text.strip()
                value = rowtd[6].text.strip()
                jsonObject[key] = value
            else:
                pass
        
        detailedVehicalData[detail_part[detail_key_id]] = jsonObject

    
    
    return detailedVehicalData

#mock reg = MP04A2300
def vehicalDetailFromRegNumber(reg_number):

    driver.implicitly_wait(10)
    driver.get("http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx")
    resgistration_input = driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_txtRegNo"]""")
    resgistration_input.send_keys(reg_number)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_btnShow"]""").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_grvSearchSummary"]/tbody/tr[2]/td[2]/input""").click()

    time.sleep(2)
    if(len(driver.current_url)>200):

        userDetails = driver.page_source
    
        soup  = BeautifulSoup(driver.page_source,'html.parser')

        mydivs = soup.findAll("td", {"class": "Same"})[0]
        
        detail_part = {
            0 : "Owner's Detail",
            1 : "Vehicle Technical Details",
            3 : "Vehicle Purchase Details",
        }


    data  = getVehicalDetailJson(mydivs,detail_part)
    return data

# jsonData = vehicalDetailFromRegNumber("MP04A2300")
# print(jsonData)

#rest api  

app = flask.Flask(__name__)

# @app.route('/',methods = ['GET'])
# def home():
#     registration_number = request.args['reg_number']
#     try:
#         jsonData = vehicalDetailFromRegNumber(registration_number)
#         return str(jsonData)
#      except KeyError:
#         return "invalid input "

@app.route('/', methods=['GET'])
def home():
    
    registration_number = request.args['reg_number']
    try:
        dictData = vehicalDetailFromRegNumber(registration_number)
        jsonData = jsonify(dictData)
        return jsonData
    except KeyError:
        return "invalid input "
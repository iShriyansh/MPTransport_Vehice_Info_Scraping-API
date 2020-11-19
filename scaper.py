from selenium import webdriver
import time
from bs4 import BeautifulSoup
import flask
from flask import request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from formatter import Formatter 
import errros



class MainClass:
     
    #Test env
    #driver = webdriver.Chrome(executable_path= "/home/shriyansh/Desktop/Mp Transport/chromedriver_linux64/chromedriver")
    
    #Prod env
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    
    
    
    data_formatter = Formatter()
   
   
    #mock reg = MP04A2300

    def vehicalDetailFromRegNumber(self,reg_number):
        driver = self.driver
        try:
            driver.implicitly_wait(10)
            driver.get("http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx")
            resgistration_input = driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_txtRegNo"]""")
            resgistration_input.send_keys(reg_number)
            driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_btnShow"]""").click()
            try:
                #have some glitchs
                element = WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, """"//*[@id="ctl00_ContentPlaceHolder1_grvSearchSummary"]/tbody/tr/td""")))  
                text = driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_grvSearchSummary"]/tbody/tr/td""").text.strip()
                if (text == "No record found......"):
                    driver.close()
                    return errros.no_record_found
            except:
                pass
            driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_grvSearchSummary"]/tbody/tr[2]/td[2]/input""").click()
            elementx = WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, """"//*[@id="ctl00_ContentPlaceHolder1_grvSearchSummary"]/tbody/tr/td"""))) 
            mydivs = soup.findAll("td", {"class": "Same"})[0]
            

            
            try:
                driver.close()
                return self.data_formatter.vehical_detail_formatter(mydivs)
            
            except:
                
                return errros.formating_error
                driver.close()

        except:
            
            return errros.internal_error
            driver.close()


#---------------------------------------------------------------------------------------------------------------------------------License------------

    

    def getDrivingLicenseDetailsByDLNumber(self,license_number,dob):
        
        driver = self.driver
        try:
            driver.implicitly_wait(10)
            driver.get("http://mis.mptransport.org/MPLogin/eSewa/DrivingLicenseSearch.aspx")
            #inputting license number
            driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_txtDrivingLicense"]""").send_keys(license_number)
            #inputting dob
            driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_txtDOB"]""").send_keys(dob)
            #clicking submit button
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_btnShow"]""").click()
            driver.implicitly_wait(10)
            msg = ""
            try:
                msg = driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_grvDrivingLicenseSummary"]/tbody/tr/td""").text
                if(msg.strip()=="No record found......"):
                    driver.close()    
                    return errros.no_record_found      
            except:
                pass
            driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_grvDrivingLicenseSummary"]/tbody/tr[2]/td[3]/a""").click()   
            element = WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.ID, "ctl00_ModalUpdateProgress1"))) 
            try:
                return self.data_formatter.formate_license_data(driver.page_source)
            except:
                
                return errros.formating_error
                driver.close()
    
        except:
            
            return errros.internal_error
            driver.close()
        
#--------------------------------------------driving license ending-------------------------------------------

    def getBusesTimeTable(self,source, destination):
        driver = self.driver
        try:
           
            driver.get("http://mis.mptransport.org/MPLogin/eSewa/NewTimeTableReport.aspx")
            #inputting source
            driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_txtsource"]""").send_keys(source)
            #inputting destination
            driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_txtdest"]""").send_keys(destination)
            #clicking submit button
            driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_btnShow"]""").click()
                 
            element = WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.ID, "ctl00_ModalUpdateProgress1")))
            try:
                msg = driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_updRto"]/table/tbody/tr[9]/td""").text
                if(msg.strip()=="No Record Found.."):
                    print(msg)
                    driver.close()    
                    return errros.no_record_found      
            except:
                pass

            try:
                return self.data_formatter.busesTimeTableFormatter(driver.page_source)
                driver.quit()
            except:
                
                return errros.formating_error
                driver.close()
    
        except:
            
            return errros.internal_error
            driver.close()
        

    def getLearningLicenseDetailsByDLNumber(self,learning_license_number):
        
        driver = self.driver
        try:
            driver.implicitly_wait(10)
            driver.get("http://mis.mptransport.org/MPLogin/eSewa/LearningLicenseSearch.aspx")
            #inputting license number
            driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_txtDrivingLicense"]""").send_keys(learning_license_number)
    
            #clicking submit button
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_btnShow"]""").click()
            driver.implicitly_wait(10)
            msg = ""
            driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_grvLearnersLicenseSummary"]/tbody/tr[2]/td[3]/a""").click()   
            element = WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.ID, "ctl00_ModalUpdateProgress1"))) 
            try:
                return self.data_formatter.formate_license_data(driver.page_source)
            except:
                
                return errros.formating_error
                driver.close()
    
        except:
            
            return errros.internal_error
            driver.close()






   


#MP51N-2019-0064688
#05/11/1999

#rest api  

# app = flask.Flask(__name__)

# @app.route('/',methods = ['GET'])
# def home():
#     registration_number = request.args['reg_number']
#     try:
#         jsonData = vehicalDetailFromRegNumber(registration_number)
#         return str(jsonData)
#     except KeyError:
#         return "invalid input "



        

    
 


        



from selenium import webdriver
import time
from bs4 import BeautifulSoup


driver = webdriver.Chrome(executable_path= "/home/shriyansh/Desktop/Mp Transport/chromedriver_linux64/chromedriver")
driver.implicitly_wait(10)
driver.get("http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx")


resgistration_input = driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_txtRegNo"]""")


resgistration_input.send_keys("MP04A2300")
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

data  = getVehicalDetailJson(mydivs,detail_part)
print(data)
        



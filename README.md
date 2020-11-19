# Mp rto scapper + api 

http://mis.mptransport.org/MPLogin/eLogin.aspx

Vehicle Registration Search,
Driving License Search,
Learning License Search,
Time Table Of Busses,

Language - python
scapper - Beautifulsoup, Selenium + chrome web_driver
server - flask 
hosting - heroku


this source code is working in both locally or in heroku 

# scaper.py
    #testing env local
        #note : dowload chrome web driver which is compatible with your browser version and set path 
        #link - https://chromedriver.chromium.org/downloads

        #self.driver = webdriver.Chrome(executable_path= "/home/shriyansh/Desktop/Mp Transport/chromedriver_linux64/chromedriver")
    
        #Prod env in heroku
        #comment it if you are using it locally
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

eg api calls - 
https://mp-rto.herokuapp.com/vehical_details/MP04A2300

https://mp-rto.herokuapp.com/bus_tt/mandla/dindori/

https://mp-rto.herokuapp.com/license_details?reg_number=MP51N-2049-0064688&dob=05/11/1979

https://mp-rto.herokuapp.com/l_license_details/MP07L009383/06/


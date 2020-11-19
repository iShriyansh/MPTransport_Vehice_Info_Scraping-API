# Mp rto scapper + api 

http://mis.mptransport.org/MPLogin/eLogin.aspx

Vehicle Registration Search
Driving License Search
Learning License Search
Time Table Of Busses

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


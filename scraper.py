from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://www.prudential.com.hk/PruServlet?module=fund&purpose=searchHistFund&fundCd=MMFU_U")

elem = browser.find_element_by_xpath('//*[@id="disclaimer"]/div/div')
elem.click()
time.sleep(0.2)

elem = browser.find_element_by_xpath("//*")
print(elem.get_attribute("outerHTML"))
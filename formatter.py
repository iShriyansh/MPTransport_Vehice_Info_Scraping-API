from bs4 import BeautifulSoup

class Formatter:

 #------------------------------------------------------License details formatter -------------------------------------
    def tableToDict(self,table_src):
        
        def chkList(lst): 
            return len(set(lst)) == 1

        table_list = []
        for i in table_src.findAll("tr"):
            single_row = []
            for j in i.findAll(["th","td"]):
                single_row.append(j.text.strip())

            if (not chkList(single_row)):     
                table_list.append(single_row)
            else:
                pass
        tabledict = {}
        for i in range(1,len(table_list)):
            tabledict[str(i)] = dict(zip(table_list[0],table_list[i]))

        return tabledict


    def formate_license_data(self,page_source):

        srccc = str(page_source).replace('<br>', '').replace('&nbsp;', '').replace('\n ', '')
        soup  = BeautifulSoup(srccc,'html.parser')
        x =  soup.findAll("div", {"id": "ctl00_ContentPlaceHolder1_pnlModel"})[0].findAll("tbody")[2].findAll("tr")
        license_details = {}
        print(len(x))
        for i in range(0,7):
            tds = x[i].findAll("td")
            key = tds[1].text.strip()
            value = tds[3].text.strip()
            license_details[key] = value

            if(len(tds)>5):
                
                key = tds[5].text.strip()
                value = tds[7].text.strip()
                license_details[key] = value
        
        try:
            user_profile_image = x[7].findAll("img",{"id":"ctl00_ContentPlaceHolder1_imgApplicantId"})[0]
            license_details["user_img"] = user_profile_image["src"]
        except:
            pass
        
        try:
            class_table = x[7].findAll("table",{"class":"Grid"})[0]
            classes_dict = self.tableToDict(class_table)
            license_details["classes"] = classes_dict
        except:
            pass

        return license_details



#-------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------Vehical details data fromatter -----------------------------------------------

    def vehical_detail_formatter(self,page_src_part):

        detail_part = {
            0 : "Owner's Detail",
            1 : "Vehicle Technical Details",
            3 : "Vehicle Purchase Details",
        }
        detailedVehicalData = {}
        for i in range(len(detail_part)):
            detail_key_id = list(detail_part)[i]
            DetailsRow = page_src_part.findAll("fieldset")[detail_key_id].findAll("tr")
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



#-----------------------------------------------------------------------------------------------------------------------------

    def busesTimeTableFormatter(self,source):
        
        cleansrc = str(source).replace('<br>', '').replace('&nbsp;', '').replace('\n ', '')
        soup =  BeautifulSoup(cleansrc,'html.parser')
        x = soup.findAll("table", {"class": "Grid"})[0]
        busesDict = self.tableToDict(x)
        return busesDict
        

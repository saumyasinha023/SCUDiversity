from selenium import webdriver
import csv
from bs4 import BeautifulSoup
import selenium.common.exceptions as sce
import time
import os
import re
from selenium.webdriver.common.action_chains import ActionChains

# time1 = time.time()
csv_count = 111
if os.path.isfile('C:\\Users\\Puneet\\PycharmProjects\\leet\\Link_air_engr'+str(csv_count)+'.csv'):
    os.remove('C:\\Users\\Puneet\\PycharmProjects\\leet\\Link_air_engr'+str(csv_count)+'.csv')
rows = []
rows.append(['Name','Title', 'Location', 'Url','ImageURL'])
url = 'https://www.linkedin.com/'
driver = webdriver.Chrome('C:\\Users\\Puneet\\Desktop\\chromedriver_win32\chromedriver.exe')
driver.get(url)
driver.maximize_window()
driver.find_element_by_class_name('login-email').send_keys('colleenchien@gmail.com')
driver.find_element_by_class_name('login-password').send_keys('6enji05')
driver.find_element_by_id('login-submit').click()
driver.execute_script("document.body.style.zoom='zoom %'")
time.sleep(2)
driver.get('https://www.linkedin.com/sales?trk=d_flagship3_nav')
time.sleep(2)

# https://www.linkedin.com/sales/search/people?geo=us%3A0&keywords=Airbnb
# https://www.linkedin.com/sales/search/people?geo=us%3A0&keywords=Airbnb&logHistory=true&logId=2720376666&page=1&searchSessionId=%2F0vRzMVIQvGMSTDTT7%2Fcjg%3D%3D&title=Software%2520Engineer%3A9%2CEngineering%2520Manager%3A174%2CAnalytics%2520Manager%3A2525%2CData%2520Scientist%3A25190%2CMachine%2520Learning%2520Engineer%3A25206%2CWeb%2520Developer%3A100%2CSystem%2520Architect%3A424%2CDatabase%2520Administrator%3A132%2CRelease%2520Manager%3A1666%2CSoftware%2520Test%2520Engineer%3A661%2CInformation%2520Security%2520Specialist%3A1801&titleTimeScope=CURRENT
# https://www.linkedin.com/sales/search/people?geo=us%3A0&keywords=Airbnb&logHistory=true&logId=2720376666&page=1&school=20129%2C20065%2C18446%2C19408%2C19360%2C18554%2C18782%2C18737%2C18064%2C164008%2C19471%2C19579%2C17738%2C3197579%2C17971%2C18321%2C18634%2C17811%2C42886%2C17926%2C18494%2C18158%2C18357%2C19232&searchSessionId=%2F0vRzMVIQvGMSTDTT7%2Fcjg%3D%3D&title=Software%2520Engineer%3A9%2CEngineering%2520Manager%3A174%2CAnalytics%2520Manager%3A2525%2CData%2520Scientist%3A25190%2CMachine%2520Learning%2520Engineer%3A25206%2CWeb%2520Developer%3A100%2CSystem%2520Architect%3A424%2CDatabase%2520Administrator%3A132%2CRelease%2520Manager%3A1666%2CSoftware%2520Test%2520Engineer%3A661%2CInformation%2520Security%2520Specialist%3A1801&titleTimeScope=CURRENT
#https://www.linkedin.com/sales/search/people?company=Airbnb%3A309694&companyTimeScope=CURRENT&geo=us%3A0&keywords=Airbnb&logHistory=true&logId=2720376666&page=1&school=164008%2C17738%2C17811%2C17926%2C17971%2C18064%2C18158%2C18321%2C18357%2C18446%2C18494%2C18554%2C18634%2C18737%2C18782%2C19232%2C19360%2C19408%2C19471%2C19579%2C20065%2C20129%2C3197579%2C42886&searchSessionId=%2F0vRzMVIQvGMSTDTT7%2Fcjg%3D%3D&title=Software%2520Engineer%3A9%2CEngineering%2520Manager%3A174%2CAnalytics%2520Manager%3A2525%2CData%2520Scientist%3A25190%2CMachine%2520Learning%2520Engineer%3A25206%2CWeb%2520Developer%3A100%2CSystem%2520Architect%3A424%2CDatabase%2520Administrator%3A132%2CRelease%2520Manager%3A1666%2CSoftware%2520Test%2520Engineer%3A661%2CInformation%2520Security%2520Specialist%3A1801&titleTimeScope=CURRENT
for j in range(1,24):

    time.sleep(2)
    driver.execute_script("document.body.style.zoom='25%'")
    driver.get('https://www.linkedin.com/sales/search/people?company=Airbnb%3A309694&companyTimeScope=CURRENT&geo=us%3A0&keywords=Airbnb&logHistory=true&logId=2720376666&page='+str(j)+'&school=17926%2C19232%2C18321%2C18494%2C17971%2C18158%2C18357%2C17811%2C42886%2C18634%2C164008%2C17738%2C18064%2C18446%2C18554%2C18737%2C18782%2C19360%2C19408%2C19471%2C19579%2C20065%2C20129%2C3197579&searchSessionId=%2F0vRzMVIQvGMSTDTT7%2Fcjg%3D%3D&title=Software%2520Engineer%3A9%2CEngineering%2520Manager%3A174%2CAnalytics%2520Manager%3A2525%2CData%2520Scientist%3A25190%2CMachine%2520Learning%2520Engineer%3A25206%2CWeb%2520Developer%3A100%2CSystem%2520Architect%3A424%2CDatabase%2520Administrator%3A132%2CRelease%2520Manager%3A1666%2CSoftware%2520Test%2520Engineer%3A661%2CInformation%2520Security%2520Specialist%3A1801%2CAnalytics%2520Consultant%3A8227%2CFrontend%2520Web%2520Developer%3A7176%2CFrontend%2520Developer%3A3172%2CBack-end%2520Developer%3A25194%2CProgrammer%2CData%2520centre%2520manager%2Crelease%2520manager%2CArtificial%2520Intelligence&titleTimeScope=CURRENT')
    driver.execute_script("document.body.style.zoom='25%'")
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(5)
    driver.execute_script("window.scrollTo(1000, document.body.scrollHeight);")
    text = BeautifulSoup(driver.page_source,'html.parser')
    results = text.find_all('li',attrs={'class':'pv5 ph2 search-results__result-item'})
    #driver.find_elements_by_xpath("//*[@id='ember949']/form/ol/li")
    #print(results)

    for index,each in enumerate(results):
        print(index)
        if(index!=0 and index%10==0):
            f = driver.get_window_size()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #print('each -->' + str(each))
        try:
            name_path = text.find_all('h4',attrs={'class':'a11y-text'})
            # print(name_path)
            profile = name_path[index*2].getText().split('-')
            # print(profile)
            name = profile[1].strip()
            print('name -->' + name)
        except sce.NoSuchElementException as e:
            name = " "
        try:
            designation_path = text.find_all('span',attrs={'class':'Sans-14px-black-75%-bold'})
            # print(designation_path)
            designation = designation_path[index].getText()
            print('designation -->' + designation)
        except sce.NoSuchElementException as e:
            designation = " "

        #name = url_path[index].getText()
        try:
            loc_path = text.find_all('li',attrs={'class':'result-lockup__misc-item'})
            location = loc_path[index].getText()
            print('location -->' + location)
        except sce.NoSuchElementException as e:
            location = " "
        # time.sleep(2)
        try:
            img_path = each.find('img', attrs={'src':re.compile('^(https://media\.licdn\.com/dms/image.+/profile-displayphoto.+)|^(data:image/.+)')})
            #img_path =each.find('img',attrs={'class': 'lazy-image result-lockup__icon loaded'})
            print(img_path)
            if (img_path is None):
                img = 'NA'
            else:
                img = img_path['src']
            print('img -->' + img)
        except sce.NoSuchElementException as e:
            img = " "
        try:
            url_path = each.find('a', attrs={'href':re.compile('^\/sales.+NAME_SEARCH.+$')})
            print(url_path)
            try:
                url = url_path['href']
                print(url)
            except sce.NoSuchElementException as e:
                url = " "
        except sce.NoSuchElementException as e:
            url =" "
        rows.append([name, designation,location , url, img])
        with open('C:\\Users\\Puneet\\PycharmProjects\\leet\\Link_air_engr'+str(csv_count)+'.csv','w',newline='') as f_output:
            csv_output = csv.writer(f_output)
            csv_output.writerows(rows)







from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

#OPENING THE WEBSITE
option=webdriver.ChromeOptions()
option.add_argument('use-fake-ui-for-media-stream')
driver=webdriver.Chrome(options=option)

driver.get('https://targetsite.com')

Privacy=driver.find_element_by_xpath('//*[@id="agree_button"]')
Privacy.click()

User_id=driver.find_element_by_xpath('//*[@id="user_id"]')
User_id.send_keys('userid')

Password=driver.find_element_by_xpath('//*[@id="password"]')
Password.send_keys('password')

Sign_in=driver.find_element_by_xpath('//*[@id="entry-login"]')
Sign_in.click()


#OPENING THE COURSES

#Link of different modules that leads to different courses
Link={'BIO':'//*[@id="course-link-_48449_1"]/h4','OOPS':'//*[@id="course-link-_52576_1"]/h4','OOPS1':'//*[@id="course-link-_52576_1"]/h4','DE':'//*[@id="course-link-_49640_1"]/h4','DE1':'//*[@id="course-link-_49640_1"]/h4','CS':'//*[@id="course-link-_53343_1"]/h4','DT':'//*[@id="course-link-_49812_1"]/h4','DT1':'//*[@id="course-link-_49812_1"]/h4','MATH':'//*[@id="course-link-_51934_1"]/h4','IP':'//*[@id="course-link-_55572_1"]/h4','WS':'//*[@id="course-link-_55083_1"]/h4','WS1':'//*[@id="course-link-_55083_1"]/h4','LSM':'//*[@id="course-link-_51325_1"]/h4'}

#time table for friday
time_table_fri={'DE':'940','OOPS':'1030','OOPS1':'1120','BIO':'1300','CS':'1350','MATH':'1440'}
arr_fri=['DE','OOPS','OOPS1','BIO','CS','MATH']

driver.maximize_window()

# I created a loop that will traverse through arr_fri and according to the time given in time_table_fri it will open and close the different courses.

#main code
j=0
for sub in arr_fri:

    if sub=="BIO":
        time.sleep(3000)

    sub1_time=time_table_fri[sub]

    if j<len(arr_fri)-1:
      sub2_time=time_table_fri[arr_fri[j+1]]
    else:
        sub2_time='1600'
    
    now =datetime.now()
    current_hour=now.strftime("%H")
    current_min=now.strftime("%M")
    current_time=current_hour+current_min

    if int(current_time)>=int(sub1_time) and int(current_time)<int(sub2_time):
        
        
        time.sleep(9)
        driver.find_element_by_xpath('//*[@id="main-content-inner"]').send_keys(Keys.END)

        time.sleep(2)
        main=driver.find_element_by_xpath(Link[sub])
        main.click()

        time.sleep(11)
        course_link=driver.find_element_by_xpath('//*[@id="sessions-list-dropdown"]/span')
        try:
            course_1=driver.find_element_by_xpath('//*[@id="sessions-list"]/li[2]/a/span')
        except:
            course_1=driver.find_element_by_xpath('//*[@id="sessions-list"]/li[1]/a/span')

        course_link.click()
        course_1.click()

        p=driver.current_window_handle
        chwd=driver.window_handles

        for w in chwd:
            if w!=p:
                driver.switch_to.window(w)

        flag=True
        try:
            time.sleep(40)
            mic=driver.find_element_by_xpath('//*[@id="dialog-description-audio"]/div[2]/button')
            mic.click()

            time.sleep(2)
            video=driver.find_element_by_xpath('//*[@id="techcheck-video-ok-button"]')
            video.click()

            time.sleep(10)
            tutorial=driver.find_element_by_xpath('//*[@id="announcement-modal-page-wrap"]/div/div[4]/button')
            tutorial.click()

            time.sleep(3)
            collab=driver.find_element_by_xpath('//*[@id="exit-tutorial"]')
            collab.click()

            flag=False
        except:
            pass
        
        if flag==False: time.sleep(2922)
        else: time.sleep(2977)
    
        driver.close()
        cw=driver.window_handles
        for k in cw:
            driver.switch_to.window(k)
    
        time.sleep(1)
        cross=driver.find_element_by_xpath('//*[@id="main-content"]/div[3]/div/div[2]/button')
        cross.click()

        j=j+1

    else:
        j=j+1
        continue
    
driver.quit()
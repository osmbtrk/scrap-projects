from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import os
import re
import time
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get('https://members.goviral.ai/login')

inputElement = driver.find_element_by_class_name("form-control")
inputElement.send_keys('mohamedaminebm@outlook.fr')

inputElement2 = driver.find_element_by_xpath("(//input[@class='form-control'])[2]")
inputElement2.send_keys('021215Ac')

driver.find_element_by_class_name('kt-login__btn-primary').click()
print('login site done')
time.sleep(5)
print("window title = " + driver.title)
#element=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH ,"//a[@href ='https://members.goviral.ai/coins']")))
#element.click()
driver.find_element_by_xpath('//a[@href ="https://members.goviral.ai/coins"]').click()          
 #signin      
#time.sleep(3) 
#driver.switch_to.window(driver.window_handles[1])

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument('window-size=1920x1480')

time.sleep(2) 
# Open a new window
# This does not change focus to the new window for the driver.
driver.execute_script("window.open('');")
time.sleep(3)
# Switch to the new window
driver.switch_to.window(driver.window_handles[1])
driver.get("https://accounts.google.com/signin")
time.sleep(3)
try:

    emailid = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='identifierId']"))) 
    
    emailid.send_keys('mallessamohamedamine@gmail.com') 
    nextButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='identifierNext']/div/button"))) 
    
    ActionChains(driver).move_to_element(nextButton).click().perform() 

    time.sleep(6) 
    mailpass = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
    mailpass.send_keys('Dropshipping     1998')

    logButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='passwordNext']/div/button"))) 
    
    ActionChains(driver).move_to_element(logButton).click().perform() 

    time.sleep(10)
except:
    print('time out, repeat')
# close the active tab
driver.close()
time.sleep(3)
# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])

#try:
#    element2=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a')))

    #element2.click()


    #emailid = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='identifierId']"))) 
    
   # emailid.send_keys('mallessamohamedamine@gmail.com') 
   # nextButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='identifierNext']/div/button"))) 
    
    #ActionChains(driver).move_to_element(nextButton).click().perform() 

 #   time.sleep(6) 
  #  mailpass = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
   # mailpass.send_keys('Dropshipping     1998')

    #logButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='passwordNext']/div/button"))) 
    
  #  ActionChains(driver).move_to_element(logButton).click().perform() 

   # time.sleep(10)
#except:
   # print('time out, repeat')


#driver.switch_to.window(driver.window_handles[0])
x=0
while True:
    print("loop begin")
    subdisable=driver.find_element_by_xpath('//*[@id="kt_content"]/div/div[1]/div/form/div/div[1]/section[1]') #pay attention: find_element
    subdisable_attribute=subdisable.get_attribute("class")
    print (str(subdisable_attribute))
    if str(subdisable_attribute)=='earn-subscribes earning-box position-relative disabled':
        print('subscribes disabled')
    else:
        print('found subscribe button')
        sub=driver.find_element_by_xpath('//*[@id="kt_content"]/div/div[1]/div/form/div/div[1]/section[1]/div[2]/div[3]/button') #pay attention: find_element
        sub_attribute=sub.get_attribute("disabled")
        print (str(sub_attribute))
        if str(sub_attribute)=='true':
            print ("wait")
        else:
            print ('ready')
            try:
                sub.click()
                time.sleep(5)
                driver.switch_to.window(driver.window_handles[2])
            except:
                pass
            print("window title = " + driver.title)
            
            #if str(driver.title) =='404 Not Found' or str(driver.title) =='YouTube':
            try:
                abonn = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='subscribe-button']/ytd-subscribe-button-renderer"))) 
                abonn.click()
                time.sleep(2)
            except:
                pass
            driver.switch_to.window(driver.window_handles[0])
            verif = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='verify-action-button']"))) 
            ActionChains(driver).move_to_element(verif).click().perform()
    likedisable=driver.find_element_by_xpath('//*[@id="kt_content"]/div/div[1]/div/form/div/div[1]/section[2]') #pay attention: find_element
    likedisable_attribute=likedisable.get_attribute("class")
    print (str(likedisable_attribute))
    if str(likedisable_attribute)=='earn-likes earning-box position-relative disabled':
        print('likes disabled')
    else:
        print('found like button')
        like=driver.find_element_by_xpath('//*[@id="kt_content"]/div/div[1]/div/form/div/div[1]/section[2]/div[2]/div[3]/button') #pay attention: find_element
        like_attribute=like.get_attribute("disabled")
        print (str(like_attribute))
        if str(like_attribute)=='true':
            print ("wait")
        else:
            print ('ready')
            try:
                like.click()
                time.sleep(5)
                driver.switch_to.window(driver.window_handles[2])
            except:
                pass
            print("window title = " + driver.title)
            
            #if str(driver.title)!='404 Not Found':
            try:
                presslike = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[8]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button"))) 
                presslike.click()
                time.sleep(2)
            except:
                pass
            driver.switch_to.window(driver.window_handles[0])
            verif = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='verify-action-button']"))) 
            ActionChains(driver).move_to_element(verif).click().perform()
    commdisable=driver.find_element_by_xpath('//*[@id="kt_content"]/div/div[1]/div/form/div/div[1]/section[3]') #pay attention: find_element
    commdisable_attribute=commdisable.get_attribute("class")
    print (str(commdisable_attribute))
    if str(commdisable_attribute)=='earn-comments earning-box position-relative disabled':
        print('comments disabled')
    else:
        print('found comment button')
        comm=driver.find_element_by_xpath('//*[@id="kt_content"]/div/div[1]/div/form/div/div[1]/section[3]/div[2]/div[3]/button') #pay attention: find_element
        comm_attribute=comm.get_attribute("disabled")
        if str(comm_attribute)=='true':
            print ("wait")
        else:
            print ('ready')
            try:
                comm.click()
                time.sleep(5)
                driver.switch_to.window(driver.window_handles[2])
            except:
                pass
            print("window title = " + driver.title)
            
            #if str(driver.title)!='404 Not Found':
            try:
                driver.execute_script('window.scrollTo(0,(window.pageYOffset+500))')
                time.sleep(5)
                comment = "amazing"

                box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "box")))
                box.click()

                frame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="+1"]')))
                driver.switch_to.frame(frame)

                driver.find_element_by_xpath('//div[@onclick]').click()

                element3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@jsname="msEQQc"]/following-sibling::div//div[@g_editable="true"]')))
                driver.execute_script("arguments[0].innerHTML='%s';" % comment, element3)
            except:
                pass
            driver.switch_to.window(driver.window_handles[0])
            verif = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='verify-action-button']"))) 
            ActionChains(driver).move_to_element(verif).click().perform()
    #/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/div/form/div/section/div/div[2]/div[1]/span
    try:
        timer=driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/div/form/div/section/div/div[2]/div[1]/span')
        timed=timer.text
        if str(timed)=='0':
            x+=1
            print('wait to press next number')
            print(x)
            if str(x)=='30':
                nextvideo = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/div/form/div/div[2]/button[1]"))) 
                nextvideo.click()
            #/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/div/form/div/div[2]/button[1]
        else:
            x=0
            print('new page')
    except:
        pass
    time.sleep(4)
#attribute_value = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "style-scope yt-icon-button"))).get_attribute("aria-pressed")
#typevalue=like.get_attribute('aaaa')
#if str(attribute_value)=='true':
    #print ("oui")
#else:
    #print ('non')
#elif driver.find_elements_by_xpath('//*[@id="kt_content"]/div/div[1]/div/form/div/div[1]/section[3]/div[2]/div[3]/button'):
    #print ("Element exists")

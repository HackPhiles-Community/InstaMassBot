####IMPORTING LIBRARY####
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import keys
import time
import os
from selenium.webdriver.remote.webelement import WebElement
 
####  SETTING UP ENVIREONMENT
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

####WEBSITE###
driver.get ( "https://www.instagram.com" )



#### FUNCTION TO LOGIN
def login(username,passward):
    time.sleep(2)
    username_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    passward_input = driver.find_element_by_xpath('//input[@name=\"password\"]')
    login_button = driver.find_element_by_xpath('//button[@type="submit"]')
    username_input.send_keys ( username )
    passward_input.send_keys ( passward )
    login_button.click ()
    time.sleep(5)
    try:
        nt_now = driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")  
        nt_now.click()
        time.sleep(3)
        not_now = driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")
        not_now.click()  
        print("LOGIN SUCESSFULLY")
    except:
        pass




### FUNCTION TO GET FOLLWERS
def follwers_list(username):
    global users
    driver.get('https://www.instagram.com/'+username+'/')
    time.sleep(5)
    num_followers=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text
    num_followers =num_followers.replace(',','')
    num_followers=int(num_followers)
    list_followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    list_followers.click()
    time.sleep(3)
    box = driver.find_element_by_class_name('isgrP')
    ht =0
    X = num_followers
    while True:
        time.sleep(2)
        ht+=5
        scroll = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight);
        return arguments[0].scrollHeight;""", box)
        if ht >=X:
            break

    links = box.find_elements_by_tag_name('a')
    users = [name.text for name in links if name.text != '']
    driver.find_element_by_xpath("//div[@class='WaOAr']//button[contains(@class,'wpO6b')]").click()


### FUNCTION TO MESSAGE TO A USER
def message(name,text):
    time.sleep(5)
    driver.get('https://www.instagram.com/'+name+'/')
    time.sleep(5)
    try:
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button').click()
    except:
        driver.find_element_by_class_name('sqdOP').click()
        time.sleep(4)
        try:
            message=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button')
            message.click()
            time.sleep(8)
            message_input=driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            message_input.send_keys(text)
            send_button=driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
            send_button.click()
            time.sleep(3)
            driver.get('https://www.instagram.com/'+name+'/')
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
        except:
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button').click()
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
        
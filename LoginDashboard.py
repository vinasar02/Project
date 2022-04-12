import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

class LoginPage:
    textbox_username_id="username"
    textbox_password_id="password"
    button_login_xpath="/html/body/div/div/div[2]/div/div/div/div/div[2]/form/div[3]/button"

    def __init__(self, driver):
        self.driver = driver

############################## LOGIN ############################################################

#set the username
    def setusername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
#set the password
    def setpassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
#click the login button
    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

############################## DASHBOARD ############################################################

#click decline card and click dashboard back
    def clickcard(self):
        dashbutton = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/h5')
        dashbutton.click()
        time.sleep(10)
        back = self.driver.find_element(By.XPATH, "/html/body/div/nav/div/div/ul[1]/li[1]/a")
        back.click()

#click the dropdown button and choose FiberCut to look the bar
    def selectbar(self):
        select = Select(self.driver.find_element_by_id("chart_type"))
        select.select_by_visible_text("Fiber Cut")
        time.sleep(5)

 #scroll down to the bottom of the page
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

# click the dropdown button and choose unmatched to look the number of data
    def reportsource(self):
        select = Select(self.driver.find_element_by_id("source_type"))
        select.select_by_visible_text("Unmatched")
        time.sleep(5)

# click any data to look on the recent worklist
    def recentworklist(self):
        pressalert = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/ul/li[1]/div")
        pressalert.click()
        time.sleep(5)
        backbutton = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button/div/span")
        backbutton.click()






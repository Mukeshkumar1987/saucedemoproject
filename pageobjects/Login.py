from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException as Ec


class LoginPage:
    Text_Username_XPATH = (By.XPATH,"//input[@id='user-name']")
    Text_Password_XPATH = (By.XPATH,"//input[@id='password']")
    click_Login_XPATH = (By.XPATH,"//input[@id='login-button']")
    click_Menu_XPATH = (By.XPATH,"//button[@id='react-burger-menu-btn']")
    click_logout_XPATH = (By.XPATH,"//a[@id='logout_sidebar_link']")



    def __init__(self,driver):
        self.driver = driver

    def  Enter_Username(self,username):
        self.driver.find_element(*LoginPage.Text_Username_XPATH).send_keys(username)

    def Enter_Password(self,password):
        self.driver.find_element(*LoginPage.Text_Password_XPATH).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPage.click_Login_XPATH).click()

    def click_Menu(self):
        self.driver.find_element(*LoginPage.click_Menu_XPATH).click()

    def click_Logout(self):
        self.driver.find_element(*LoginPage.click_logout_XPATH).click()

    def login_status(self):
        self.driver.implicitly_wait(5)
        try:
            self.driver.find_element(*LoginPage.click_Menu_XPATH)
            return True
        except Ec:
            return False
    #
    # def Title(self):
    #     self.driver.implicitly_wait(10)
    #     try:
    #         title = self.driver.title
    #         return True
    #     except Ec:
    #         title = self.driver.title
    #         return False
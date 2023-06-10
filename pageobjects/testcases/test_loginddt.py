import time

from pageobjects.Login import LoginPage
from pageobjects.utility import XLutils
from pageobjects.utility.Readproperties import Readconfig
import openpyxl

class Test_Login_DDT:
    url = Readconfig.geturl()
    # username = Readconfig.getusername()
    # password = Readconfig.getpassword()
    path = "C:\\Users\\mukes\\PycharmProjects\\SauceDemo\\pageobjects\\testcases\\TestData\\login.xlsx"

    def test_login_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        self.rows = XLutils.getrowCount(self.path,'Sheet1')
        status_list = []
        for r in range(2,self.rows+1):
            self.username = XLutils.readData(self.path,'Sheet1',r,2)
            self.password = XLutils.readData(self.path,'Sheet1',r,3)
            self.lp.Enter_Username(self.username)
            self.lp.Enter_Password(self.password)
            self.lp.click_login()
            if self.lp.login_status() == True:
                self.lp.click_Menu()
                self.lp.click_Logout()
                time.sleep(3)
                status_list.append("Pass")
                XLutils.writeData(self.path,'Sheet1',r,4,'Pass')
                assert True
            else:
                status_list.append("Fail")
                XLutils.writeData(self.path,'Sheet1',r,4,'Fail')
                assert False
        # print(status_list)
        # if "Fail" not in status_list:
        #     assert True
        # else:
        #     assert False




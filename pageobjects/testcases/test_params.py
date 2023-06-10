import time

from pageobjects.Login import LoginPage
from pageobjects.Productss import Products
from pageobjects.utility.Readproperties import Readconfig


class Test_Login_Params:
   url = Readconfig.geturl()
   username = Readconfig.getusername()
   password = Readconfig.getpassword()


   def test_login_params03(self,setup,getDataforlogin):
      self.driver = setup
      self.driver.get(self.url)
      self.lp = LoginPage(self.driver)
      self.lp.Enter_Username(getDataforlogin[0])
      self.lp.Enter_Password(getDataforlogin[1])
      self.lp.click_login()
      if self.lp.login_status() == True:
         if getDataforlogin[2] == 'Pass':
            self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\SauceDemo\\Screenshot\\test_params.py-pass.png")
            self.lp.click_Menu()
            self.lp.click_Logout()
            assert True
         else:
            self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\SauceDemo\\Screenshot\\test_params.py-fail.png")
            assert False
      else:
         if getDataforlogin[2] == 'Fail':
            assert True
         else:
            self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\SauceDemo\\Screenshot\\test_params.py-fail.png")
            assert False
      self.driver.close()






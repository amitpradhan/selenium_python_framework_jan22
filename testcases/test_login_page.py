from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pageobjects.LoginPage import LoginPage
from utilities.read_properties import Read_Config
from utilities.Custom_Logger import Log_Gen


class Test_Login_Page:
    app_url = Read_Config.get_app_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Gen.generate_log()

    def test_login(self,setup):
        self.logger.info("****************test_login started************************")
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = setup
        self.driver.get(self.app_url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.enter_user_name(self.username)
        self.login_page.enter_password(self.password)
        self.login_page.click_login()
        title = self.driver.title
        if self.driver.title == "Swag Labs" and self.driver.current_url == "https://www.saucedemo.com/inventory.html":
            assert True
            self.driver.close()
            self.logger.info("****************test_login passed************************")
        else:
            self.driver.save_screenshot("..\\screenshot\\" + "test_login.png")
            self.driver.close()
            self.logger.info("****************test_login failed************************")
            assert False



    def test_login_page_title(self,setup):
        self.logger.info("****************test_login_page_title started************************")
        self.driver = setup
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.app_url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        if self.driver.title == "Swag Labs":
            assert True
            self.driver.close()
            self.logger.info("****************test_login_page_title passed************************")
        else:
            self.driver.save_screenshot("..\\screenshot\\" + "test_login_page_title.png")
            self.driver.close()
            self.logger.info("****************test_login_page_title failed************************")
            assert False


# def test_login2(self):
#     self.driver = webdriver.Chrome(ChromeDriverManager().install())
#     self.driver.get(self.app_url)
#     self.driver.implicitly_wait(10)
#     self.driver.maximize_window()
#     self.login_page = LoginPage(self.driver)
#     self.login_page.login(self.username,self.password)
#     assert self.driver.title == "Swag Labs"
#     assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
#     self.driver.quit()

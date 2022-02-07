from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_submit_name = "login-button"

    def __init__(self, driver):
        self.driver = driver

    def enter_user_name(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.NAME, self.button_submit_name).click()

    def login(self, username, password):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
        self.driver.find_element(By.NAME, self.button_submit_name).click()

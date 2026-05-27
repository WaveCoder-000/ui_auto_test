from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.settings import LOGIN_URL, USERNAME, PASSWORD

class LoginPage(BasePage):
    # 正确的元素定位器（基于实际页面结构）
    USERNAME_INPUT = (By.NAME, "username")          # 用户名输入框
    PASSWORD_INPUT = (By.NAME, "password")          # 密码输入框
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., '登录')]")   # 登录按钮（通过文本定位）
    # SUCCESS_INDICATOR = (By.XPATH, "//div[contains(text(), '首页')]")  # 登录成功后的特征元素（请根据实际调整）

    def goto_login_page(self):
        """打开登录页"""
        self.open_url(LOGIN_URL)

    def input_username(self, username):
        wait = WebDriverWait(self.driver, 10)
        username_input = wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        # 强制清空 value 属性
        self.driver.execute_script("arguments[0].value = '';", username_input)
        username_input.send_keys(username)

    def input_password(self, password):
        """输入密码（带清空和等待）"""
        wait = WebDriverWait(self.driver, 10)
        password_input = wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)

    def click_login_btn(self):
        """点击登录按钮"""
        wait = WebDriverWait(self.driver, 10)
        login_btn = wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_btn.click()

    def login(self, username=USERNAME, password=PASSWORD):
        """执行完整登录操作"""
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()

    def is_login_success(self):
        return "/home" in self.driver.current_url
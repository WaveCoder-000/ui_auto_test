from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.settings import EXPLICIT_WAIT
import os
from datetime import datetime

class BasePage:
    """所有页面对象的基类"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def open_url(self, url):
        """打开 URL"""
        self.driver.get(url)

    def find_element(self, locator):
        """等待元素可见并返回"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        """等待所有元素可见"""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        """点击元素"""
        self.find_element(locator).click()

    def input_text(self, locator, text):
        """输入文本（先清空）"""
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        """获取元素文本"""
        return self.find_element(locator).text

    def wait_for_url_contains(self, partial_url):
        """等待 URL 包含指定字符串"""
        self.wait.until(EC.url_contains(partial_url))

    def is_element_visible(self, locator, timeout=EXPLICIT_WAIT):
        """判断元素是否可见（不抛异常）"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def take_screenshot(self, name="screenshot"):
        """截图并保存到 screenshots 目录"""
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        return filename
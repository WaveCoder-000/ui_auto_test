from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.settings import EXPLICIT_WAIT
import os
from datetime import datetime
import time

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
    #点击复用

    # 要点击就用element_to_be_clickable，
    # 只填数据用presence_of_element_located就够用了”
    def click_element(self, locator):
        """通用方法：等待元素可点击并执行点击"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator),
            message = f"等待元素可点击超时！定位器是: {locator}"
        ).click()

    def fill_input(self, locator, value):
        """通用方法：强制清空输入框并填充新值，同时触发 Vue/React 响应事件"""
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        # 滚动到可见 居中显示
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.2)

        # 核心修改：先强制清空，再赋值
        self.driver.execute_script("""
               // 1. 强制将 value 设为空字符串（物理清空）
               arguments[0].value = '';
               // 2. 触发 input 和 change 事件（通知 Vue/React 框架同步更新内部状态）
               arguments[0].dispatchEvent(new Event('input', {bubbles: true}));
               arguments[0].dispatchEvent(new Event('change', {bubbles: true}));

               // 3. 填入新的目标值
               arguments[0].value = arguments[1];
               // 4. 再次触发事件，让框架感知到新值的输入
               arguments[0].dispatchEvent(new Event('input', {bubbles: true}));
               arguments[0].dispatchEvent(new Event('change', {bubbles: true}));
               arguments[0].dispatchEvent(new Event('blur', {bubbles: true}));
           """, element, value)
        time.sleep(0.5)

    def add_fill_input(self, locator, value):
        """通用方法：滚动居中 -> 暴力清空 -> 模拟键盘输入"""
        # 1. 等待元素出现并定位
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

        # 2. 滚动到屏幕中间，防止被遮挡
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.2)  # 等待滚动动画停止

        # 3. 核心逻辑：先用 JS 暴力清空输入框（解决编辑时旧值残留问题）
        self.driver.execute_script("arguments[0].value = '';", element)

        # 4. 再用 Selenium 的 send_keys 输入新值（保证 Vue/React 框架能识别）
        element.send_keys(value)

        time.sleep(0.3)  # 稳定等待
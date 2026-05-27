from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys   # 添加这一行
from pages.base_page import BasePage
import time

class SearchAndDelete(BasePage):
    SEARCH_PRO=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div[1]/div/div[2]/form/div[1]/div/div/div/input")
    PRO_NUMBER=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div[1]/div/div[2]/form/div[2]/div/div/div/input")
    SEARCH_BTN=(By.XPATH,"//span[text()=' 查询结果 ']/ancestor::button")
    DELETE_BTN=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[11]/div/p[2]/button[2]")
    RESET_BTN=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div[1]/div/div[1]/button[2]")

    def _fill_input(self, locator, value):
        """通用方法：填充输入框并触发 Vue 事件"""
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        # 滚动到可见
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.2)
        # 使用 JS 设置 value 并触发事件
        self.driver.execute_script("""
               arguments[0].value = arguments[1];
               arguments[0].dispatchEvent(new Event('input', {bubbles: true}));
               arguments[0].dispatchEvent(new Event('change', {bubbles: true}));
               arguments[0].dispatchEvent(new Event('blur', {bubbles: true}));
           """, element, value)
        time.sleep(0.3)

    def search_info(self, data: dict):
        if "product_name" in data:
            self._fill_input(self.SEARCH_PRO, data["product_name"])
        if "product_number" in data:
            self._fill_input(self.PRO_NUMBER, data["product_number"])

    def search_btn(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_BTN)
        )
        btn.click()
        time.sleep(1)


    def delete_btn(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DELETE_BTN)
        )
        btn.click()

    def reset_btn(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.RESET_BTN)
        )
        btn.click()

    def select_brand(self, brand_name: str):
        """选择商品品牌（使用 JS 强制点击，确保下拉打开）"""
        # 1. 定位下拉框的触发区域（el-select__wrapper）
        trigger_xpath = "/html/body/div[1]/div/div/div[2]/section/div/div[1]/div/div[2]/form/div[4]/div/div/div"
        trigger = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, trigger_xpath))
        )
        trigger.click()
        option_xpath = f"//span[text()='{brand_name}']"
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )
        option.click()
        time.sleep(0.3)

    def up_status(self,up_status:str):
        up_status_xpath="/html/body/div[1]/div/div/div[2]/section/div/div[1]/div/div[2]/form/div[5]/div/div/div"
        trigger = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, up_status_xpath))
        )
        trigger.click()
        option_xpath = f"//span[text()='{up_status}']"
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )
        option.click()
        time.sleep(0.3)


        #有问题
    def review_status(self, review_status:str):
        review_status="/html/body/div[1]/div/div/div[2]/section/div/div[1]/div/div[2]/form/div[6]/div/div/div"
        trigger = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, review_status))
        )
        trigger.click()
        option_xpath = f"//span[text()='{review_status}']"
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )

        print("选项文本:", option.text)
        option.click()
        time.sleep(0.3)

    def select_category(self, category_name: list):
        pro_sort_xpath="/html/body/div[1]/div/div/div[2]/section/div/div[1]/div/div[2]/form/div[3]/div/div"
        pro_sort = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, pro_sort_xpath))
        )
        pro_sort.click()
        for cat in category_name:
            # 等待选项可见
            option_locator = (By.XPATH, f"//span[text()='{cat}']")

            option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(option_locator)
            )
            option.click()
            # 如果是多级，可能需要短暂等待下级菜单出现
            time.sleep(0.3)  # 酌情使用显式等待也可

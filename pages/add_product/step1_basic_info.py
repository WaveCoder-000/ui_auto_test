from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class Step1BasicInfo(BasePage):
    # 商品分类相关定位器
    CATEGORY_INPUT = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[2]/form/div[1]/div/div[1]/div/div/input")
    PRODUCT_NAME=(By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[2]/form/div[2]/div/div[1]/div/input")
    TITLE=(By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[2]/form/div[3]/div/div[1]/div/input")

    PRODUCT_BRAND = (By.CSS_SELECTOR, "div.el-select:has(div.el-select__wrapper)")

    PRO_INTRODUCE=(By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[2]/form/div[5]/div/div/textarea")
    PRO_NUMBER=(By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[2]/form/div[6]/div/div/div/input")
    PRO_PRICE=(By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[2]/form/div[7]/div/div/div/input")
    MARKET_PRICE=(By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[2]/form/div[8]/div/div/div/input")
    PRO_STOCK=(By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[2]/form/div[9]/div/div/div/input")
    CALCULATE=(By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[2]/form/div[10]/div/div/div/input")
    PRO_WEIGHT=(By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[2]/form/div[11]/div/div/div/input")
    SORT=(By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[2]/form/div[12]/div/div/div/input")
    NET_BTN=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[2]/form/div[13]/div/div/button/span")


    # 注意：下拉选项的定位器需要根据实际页面调整，以下为示例：
    # 一级分类选项（通用方法中动态拼接）
    # 例如：一级分类定位器可以是 (By.XPATH, "//span[text()='服装']")\

    def net_btn(self):
        wait = WebDriverWait(self.driver, 10)
        product_list_btn = wait.until(EC.element_to_be_clickable(self.NET_BTN))
        product_list_btn.click()

    def select_category(self, category_path: list):
        """
        选择商品分类，支持多级
        category_path: 列表，如 ['服装', '外套']
        """
        # 1. 打开商品分类下拉
        wait = WebDriverWait(self.driver, 10)
        category_input =wait.until(EC.element_to_be_clickable(self.CATEGORY_INPUT))
        category_input.click()
        # 2. 逐级选择
        for cat in category_path:
            # 等待选项可见
            option_locator = (By.XPATH, f"//span[text()='{cat}']")

            option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(option_locator)
            )
            option.click()
            # 如果是多级，可能需要短暂等待下级菜单出现
            time.sleep(0.3)  # 酌情使用显式等待也可

    def select_brand(self, brand_path: list):
        """
        选择商品分类，支持多级
        category_path: 列表，如 ['服装', '外套']
        """
        # 1. 打开商品分类下拉
        wait = WebDriverWait(self.driver, 10)
        brand_input =wait.until(EC.element_to_be_clickable(self.PRODUCT_BRAND))
        brand_input.click()
        # 2. 逐级选择
        for cat in brand_path:
            # 等待选项可见
            option_locator = (By.XPATH, f"//span[text()='{cat}']")
            option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(option_locator)
            )
            option.click()

    def fill_base_info(self, data: dict):
        # 商品名称
        if "product_name" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRODUCT_NAME))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["product_name"])
        # 副标题
        if "subtitle" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.TITLE))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["subtitle"])
        # 商品介绍
        if "product_introduce" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRO_INTRODUCE))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["product_introduce"])
        # 商品货号
        if "product_number" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRO_NUMBER))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["product_number"])
        # 商品售价
        if "price" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRO_PRICE))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["price"])
        # 市场价
        if "market_price" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.MARKET_PRICE))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["market_price"])
        # 商品库存
        if "stock" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRO_STOCK))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["stock"])
        # 计量单位
        if "unit" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CALCULATE))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["unit"])
        # 商品重量
        if "weight" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRO_WEIGHT))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["weight"])
        # 排序
        if "sort" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SORT))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["sort"])

    # def fill_base_info(self,data:dict):
    #     wait = WebDriverWait(self.driver, 10)
    #
    #     # 商品名称
    #     if "product_name" in data:
    #         self.input_text(self.PRODUCT_NAME, data["product_name"])
    #     # 副标题
    #     if "subtitle" in data:
    #         self.input_text(self.TITLE, data["subtitle"])
    #     # 商品介绍
    #     if "product_introduce" in data:
    #         self.input_text(self.PRO_INTRODUCE, data["product_introduce"])
    #     # 商品货号
    #     if "product_number" in data:
    #         self.input_text(self.PRO_NUMBER, data["product_number"])
    #     # 商品售价
    #     if "price" in data:
    #         self.input_text(self.PRO_PRICE, data["price"])
    #     # 市场价
    #     if "market_price" in data:
    #         self.input_text(self.MARKET_PRICE, data["market_price"])
    #     # 商品库存
    #     if "stock" in data:
    #         self.input_text(self.PRO_STOCK, data["stock"])
    #     # 计量单位
    #     if "unit" in data:
    #         self.input_text(self.CALCULATE, data["unit"])
    #     # 商品重量
    #     if "weight" in data:
    #         self.input_text(self.PRO_WEIGHT, data["weight"])
    #     # 排序
    #     if "sort" in data:
    #         self.input_text(self.SORT, data["sort"])
    #

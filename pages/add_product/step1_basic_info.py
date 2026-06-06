from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class Step1BasicInfo(BasePage):
    # 商品分类相关定位器
    from path.product.add_product import (
        CATEGORY_INPUT,
        PRODUCT_NAME,
        TITLE,
        PRODUCT_BRAND,
        PRO_INTRODUCE,
        PRO_NUMBER,
        PRO_PRICE,
        MARKET_PRICE,
        PRO_STOCK,
        CALCULATE,
        PRO_WEIGHT,
        SORT,
        NET_BTN1
    )

    def select_category(self, category_path: list):
        self.click_element(self.CATEGORY_INPUT)
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
        self.click_element(self.PRODUCT_BRAND)
         # 2. 逐级选择
        for cat in brand_path:
            # 等待选项可见
            option_locator = (By.XPATH, f"//span[text()='{cat}']")
            option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(option_locator)
            )
            option.click()

    def fill_base_info(self, data: dict):
        """填写商品基础信息"""
        if "product_name" in data:
            self.add_fill_input(self.PRODUCT_NAME, data["product_name"])
        if "subtitle" in data:
            self.add_fill_input(self.TITLE, data["subtitle"])
        if "product_introduce" in data:
            self.add_fill_input(self.PRO_INTRODUCE, data["product_introduce"])
        if "product_number" in data:
            self.add_fill_input(self.PRO_NUMBER, data["product_number"])
        if "price" in data:
            self.add_fill_input(self.PRO_PRICE, data["price"])
        if "market_price" in data:
            self.add_fill_input(self.MARKET_PRICE, data["market_price"])
        if "stock" in data:
            self.add_fill_input(self.PRO_STOCK, data["stock"])
        if "unit" in data:
            self.add_fill_input(self.CALCULATE, data["unit"])
        if "weight" in data:
            self.add_fill_input(self.PRO_WEIGHT, data["weight"])
        if "sort" in data:
            self.add_fill_input(self.SORT, data["sort"])

    def net_btn(self):
       self.click_element(self.NET_BTN1)


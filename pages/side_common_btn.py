from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CommonPage(BasePage):
    from path.product.common import (PRODUCT,PRODUCT_LIST,ADD_PRODUCT,PRODUCT_SORT,PRODUCT_STYLE,BRAND_MANAGE)
    def product(self):
        self.click_element(self.PRODUCT)
        return "/pms/product" in self.driver.current_url

    def product_list(self):
        self.click_element(self.PRODUCT_LIST)
        return "/pms/product" in self.driver.current_url

    def add_product(self):
        self.click_element(self.ADD_PRODUCT)
        return "/pms/addProduct" in self.driver.current_url

    def product_sort(self):
        self.click_element(self.PRODUCT_SORT)
        return "/pms/productCate" in self.driver.current_url

    def product_style(self):
        self.click_element(self.PRODUCT_STYLE)
        return "/pms/productAttr" in self.driver.current_url

    def brand_manage(self):
        self.click_element(self.BRAND_MANAGE)
        return "/pms/brand" in self.driver.current_url
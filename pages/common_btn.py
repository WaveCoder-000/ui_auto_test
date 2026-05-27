from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CommonPage(BasePage):
    PRODUCT=(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/ul/div/li[2]/div/span")
    PRODUCT_LIST=(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/ul/div/li[2]/ul/a[1]/li/span")
    ADD_PRODUCT=(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/ul/div/li[2]/ul/a[2]/li/span")
    PRODUCT_SORT=(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/ul/div/li[2]/ul/a[3]/li/span")
    PRODUCT_STYLE=(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/ul/div/li[2]/ul/a[4]/li/span")
    BRAND_MANAGE=(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/ul/div/li[2]/ul/a[5]/li/span")


    def product(self):
        wait = WebDriverWait(self.driver, 10)
        product_list_btn = wait.until(EC.element_to_be_clickable(self.PRODUCT))
        product_list_btn.click()
        return "/pms/product" in self.driver.current_url

    def product_list(self):
        wait = WebDriverWait(self.driver, 10)
        product_list_btn= wait.until(EC.element_to_be_clickable(self.PRODUCT_LIST))
        product_list_btn.click()
        return "/pms/product" in self.driver.current_url

    def add_product(self):
        wait = WebDriverWait(self.driver, 10)
        product_list_btn= wait.until(EC.element_to_be_clickable(self.ADD_PRODUCT))
        product_list_btn.click()
        return "/pms/addProduct" in self.driver.current_url

    def product_sort(self):
        wait = WebDriverWait(self.driver, 10)
        product_list_btn= wait.until(EC.element_to_be_clickable(self.PRODUCT_SORT))
        product_list_btn.click()
        return "/pms/productCate" in self.driver.current_url

    def product_style(self):
        wait = WebDriverWait(self.driver, 10)
        product_list_btn= wait.until(EC.element_to_be_clickable(self.PRODUCT_STYLE))
        product_list_btn.click()
        return "/pms/productAttr" in self.driver.current_url

    def brand_manage(self):
        wait = WebDriverWait(self.driver, 10)
        product_list_btn= wait.until(EC.element_to_be_clickable(self.BRAND_MANAGE))
        product_list_btn.click()
        return "/pms/brand" in self.driver.current_url
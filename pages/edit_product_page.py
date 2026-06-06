from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys   # 添加这一行
from pages.base_page import BasePage
import time

class EditProductPage(BasePage):
    EDIT_BTN=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[11]/div/p[1]/button[2]")

    def edit_btn(self):
        self.click_element(self.EDIT_BTN)
        time.sleep(1)
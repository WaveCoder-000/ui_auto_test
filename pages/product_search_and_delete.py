from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class SearchAndDelete(BasePage):
    from path.product.common import(SEARCH_PRO_PATH,PRO_NUMBER_PATH,SEARCH_BTN,
                                    DELETE_BTN,RESET_BTN,UP_STATUS_PATH,REVIEW_STATUS_PATH,PRO_SORT_PATH,TRIGGER_PATH)

    def search_info(self, data: dict):
        if "product_name" in data:
            self.fill_input(self.SEARCH_PRO_PATH, data["product_name"])
        if "product_number" in data:
            self.fill_input(self.PRO_NUMBER_PATH, data["product_number"])

    def select_brand(self, brand_name: str):
        """选择商品品牌（使用 JS 强制点击，确保下拉打开）"""
        self.click_element(self.TRIGGER_PATH)
        option_xpath = f"//span[text()='{brand_name}']"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()
        time.sleep(0.3)


    def up_status(self,up_status:str):
        self.click_element(self.UP_STATUS_PATH)
        option_xpath = f"//span[text()='{up_status}']"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()
        time.sleep(0.3)

        #有问题
    def review_status(self, review_status:str):
        self.click_element(self.REVIEW_STATUS_PATH)
        option_xpath = f"//span[text()='{review_status}']"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()
        time.sleep(0.3)

    def select_category(self, category_name: list):
        self.click_element(self.PRO_SORT_PATH)
        for cat in category_name:
            # 等待选项可见
            option_locator = (By.XPATH, f"//span[text()='{cat}']")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(option_locator)
            ).click()
            time.sleep(0.3)  # 酌情使用显式等待也可

    def get_search_results(self):
        from selenium.webdriver.common.by import By
        import time
        time.sleep(1)
        rows = self.driver.find_elements(By.CSS_SELECTOR, ".el-table__body-wrapper tbody tr")
        results = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 5:
                # 商品名称列：取第一行（去掉换行后的品牌等信息）
                full_name = cells[3].text.strip()
                name = full_name.split('\n')[0]  # 只取第一个换行前的内容

                # 价格/货号列：例如 "¥199\n货号:123456"
                price_number = cells[4].text.strip()
                number = ""
                if "货号：" in price_number:
                    # 提取 "货号：" 后的数字
                    number = price_number.split("货号：")[-1].split('\n')[0].strip()
                results.append({"name": name, "number": number})
        return results

    def search_btn(self):
        self.click_element(self.SEARCH_BTN)

    def delete_btn(self):
        self.click_element(self.DELETE_BTN)

    def reset_btn(self):
        self.click_element(self.RESET_BTN)

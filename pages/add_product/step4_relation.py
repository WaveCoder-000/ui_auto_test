from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class Step4BasicInfo(BasePage):
    # 元素定位器（基于文本和结构）
    TOPIC_CHECKBOX = (By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[5]/form/div[1]/div[2]/div/div[1]/div/div[1]/div/input")
    MOVE_RIGHT_BTN = (By.XPATH, "//div[contains(@class,'el-transfer')]//button[contains(@class,'el-transfer__button')][2]")
    NET_BTN=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[5]/form/div[3]/div/div/button[2]")

    def select_all_right(self, check: bool = True):
        """
        勾选或取消右侧“已选择”区域的全选复选框
        :param check: True 勾选，False 取消勾选
        """
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[contains(@class,'el-checkbox') and .//span[contains(text(),'已选择')]]"))
        )
        is_checked = "is-checked" in checkbox.get_attribute("class")
        if is_checked != check:
            checkbox.click()

    def move_topic_to_right(self, topic_name: str):
        # 1. 输入搜索关键词
        search_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TOPIC_CHECKBOX)
        )
        search_input.clear()
        search_input.send_keys(topic_name)
        # 等待搜索结果加载（可根据实际情况等待复选框出现）
        time.sleep(1)  # 更好的方式是等待结果列表更新，可改为等待元素出现

        # 2. 定位并勾选目标专题的复选框（点击可见的 label 区域）
        checkbox_label = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//label[contains(@class,'el-checkbox') and .//span[contains(text(),'{topic_name}')]]"))
        )
        input_elem = checkbox_label.find_element(By.XPATH, ".//input")
        # 强制设为选中
        self.driver.execute_script("arguments[0].checked = true;", input_elem)
        # 同时触发 change 事件，让 UI 同步
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", input_elem)
        print(f"已强制勾选专题: {topic_name}")

        # 3. 点击右箭头移动

        move_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'el-transfer')]//button[contains(@class,'el-transfer__button')][2]"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", move_btn)
        time.sleep(0.2)
        self.driver.execute_script("arguments[0].click();", move_btn)

        print("已点击右箭头移动，右侧出现专题")

    def complete_btn(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.NET_BTN)).click()

        # 等待确认弹框出现，并点击“确定”按钮
        confirm_btn = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div/div[3]/button[2]"))
        )
        confirm_btn.click()
        time.sleep(5)
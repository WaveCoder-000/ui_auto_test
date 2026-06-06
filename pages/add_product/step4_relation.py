from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class Step4BasicInfo(BasePage):
    # 元素定位器（基于文本和结构）
    from path.product.add_product import (TOPIC_CHECKBOX,NET_BTN,RIGHT_CHECKBOX_PATH,RIGHT_BTN_PATH)

    def __init__(self, driver):
        super().__init__(driver)
        self.parent = None

    def select_all_right(self, check: bool = True):
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.RIGHT_CHECKBOX_PATH)
        )
        is_checked = "is-checked" in checkbox.get_attribute("class")
        if is_checked != check:
            checkbox.click()

    def move_topic(self, topic_name: str):
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
    def right_btn(self):
        # 定位向右移动按钮（第二个按钮）
        move_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.RIGHT_BTN_PATH)
        )
        # 调用强制点击函数（需要传入 driver 和元素）
        self._force_click(move_btn)
        print("已点击右箭头移动，右侧出现专题")
        time.sleep(0.5)

    def _force_click(self, element):
        """强制点击元素，绕过 Vue 的事件拦截"""
        self.driver.execute_script("""
            var el = arguments[0];
            var events = ['mousedown', 'mouseup', 'click'];
            events.forEach(function(eventType) {
                var evt = new MouseEvent(eventType, {
                    view: window,
                    bubbles: true,
                    cancelable: false,
                    buttons: 1
                });
                el.dispatchEvent(evt);
            });
            el.click();
        """, element)

    def complete_btn(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.NET_BTN)).click()

        # 等待确认弹框出现，并点击“确定”按钮
        confirm_btn = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div/div[3]/button[2]"))
        )
        confirm_btn.click()
        time.sleep(1)

    # 在 Step4BasicInfo 或其他类中
    def get_success_message(self):
        """获取操作成功后的提示文字（toast或顶部提示）"""
        try:
            # mall 后台常见：.el-message--success .el-message__content
            msg_elem = self.driver.find_element(By.CSS_SELECTOR, ".el-message--success .el-message__content")
            return msg_elem.text
        except:
            return ""
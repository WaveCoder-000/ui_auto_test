from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class Step2BasicInfo(BasePage):
    GIFT_POINT=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[1]/div/div/div/input")
    GIFT_GROWTH=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[2]/div/div/div/input")
    GIFT_BUY=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[3]/div/div/div/input")

    # # 推荐：找到包含“预告商品”文字的 label，然后定位其同级的开关
    # SWITCH_PREVIEW = (By.XPATH,
    #                   "//label[contains(text(),'预告商品')]/following-sibling::div//div[contains(@class,'el-switch')]")
    # PRO_UP=(By.XPATH,"")
    # PRO_RECOMMEND=(By.XPATH,"")
    # SERVER_ENSURE=(By.XPATH,"")

    DETAIL_TITLE=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[8]/div/div/div/input")
    DETAIL_DESCRIPTION=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[9]/div/div/div/input")
    PRO_KEY=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[10]/div/div/div/input")
    PRO_NOTE=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[11]/div/div/textarea")

    SELECT_WAY_DISCOUNT=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[12]/div/div/label[2]/span")
    NET_BTN=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[17]/div/div/button[2]/span")

    def fill_base_info(self, data: dict):
        # 赠送积分
        if "gift_point" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.GIFT_POINT))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["gift_point"])
        # 赠送成长值
        if "gift_growth" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.GIFT_GROWTH))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["gift_growth"])
        # 积分购买限制
        if "gift_buy" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.GIFT_BUY))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["gift_buy"])
        # 详细页标题
        if "detail_title" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.DETAIL_TITLE))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["detail_title"])
        # 详细页描述
        if "detail_description" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.DETAIL_DESCRIPTION))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["detail_description"])
        # 商品关键字
        if "pro_key" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRO_KEY))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["pro_key"])
        # 商品备注
        if "pro_note" in data:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRO_NOTE))
            self.driver.execute_script("arguments[0].value = '';", elem)
            elem.send_keys(data["pro_note"])

    # def set_preview_switch(self, turn_on: bool):
    #     switch = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SWITCH_PREVIEW))
    #     is_checked = switch.get_attribute("aria-checked") == "true"
    #     if is_checked != turn_on:
    #         switch.click()

    # # 商品推荐开关（通过文本定位，通用）
    # def set_recommend_switch(self, label: str, turn_on: bool):
    #     """
    #     label: '新品' 或 '推荐'
    #     turn_on: True 表示开启，False 表示关闭
    #     """
    #     # 找到文本等于 label 的 span，然后取紧随其后的 div 开关
    #     switch_locator = (By.XPATH, f"//span[text()='{label}']/following-sibling::div[contains(@class,'el-switch')]")
    #     switch = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(switch_locator))
    #     # 获取当前状态（通过 aria-checked 属性）
    #     is_checked = switch.get_attribute("aria-checked") == "true"
    #     if is_checked != turn_on:
    #         switch.click()
    #
    # def get_recommend_switch_state(self, label: str) -> bool:
    #     """获取指定开关的当前状态（True=开启）"""
    #     switch_locator = (By.XPATH, f"//span[text()='{label}']/following-sibling::div[contains(@class,'el-switch')]")
    #     switch = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(switch_locator))
    #     return switch.get_attribute("aria-checked") == "true"

    def set_switch_by_label(self, label: str, turn_on: bool):
        """
        根据标签文本操作开关（支持：预告商品、商品上架、新品、推荐）
        :param label: 文本，如 "预告商品"、"商品上架"、"新品"、"推荐"
        :param turn_on: True=开启, False=关闭
        """
        # 处理冒号（预告商品和商品上架的标签带冒号，但用户可能输入不带冒号）
        if label in ["预告商品", "商品上架"]:
            # 添加冒号以匹配实际 label 文本
            full_label = f"{label}："
            xpath = f"//label[text()='{full_label}']/following-sibling::div//div[contains(@class,'el-switch')]"
        else:  # 新品、推荐
            xpath = f"//span[text()='{label}']/following-sibling::div[contains(@class,'el-switch')]"

        switch = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        # 获取当前状态
        is_checked = switch.get_attribute("aria-checked") == "true"
        if is_checked != turn_on:
            switch.click()


    #复选框
    def set_service_checkbox(self, service_name: str, check: bool = True):
        """
        设置服务保证复选框的状态（无忧退货、快速退款、免费包邮）
        :param service_name: 服务名称，如 "无忧退货"
        :param check: True 表示勾选，False 表示取消勾选
        """
        # 定位到对应的复选框所在 label 元素
        label_locator = (By.XPATH, f"//span[@class='el-checkbox__label' and text()='{service_name}']/..")
        label = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(label_locator))
        # 获取当前是否已选中（通过判断父级 label 是否包含 'is-checked' 类，或查看原生 input 的 checked 属性）
        is_checked = "is-checked" in label.get_attribute("class")
        if is_checked != check:
            label.click()

    def select_promotion_type(self, type_text: str):
        """选择优惠方式，type_text 如 '无优惠', '特惠促销', '会员价格', '阶梯价格', '满减价格'"""
        locator = (By.XPATH, f"//label[contains(@class, 'el-radio-button') and .//span[text()='{type_text}']]")
        radio = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        radio.click()

    def set_field(self, field_name: str, value: str):
        """
        通用方法：设置促销第二步中的字段值
        :param field_name: 字段名称，支持 '开始时间', '结束时间', '促销价格'
        :param value: 要填入的值
        """
        # 根据字段名确定 placeholder 定位器
        placeholder_map = {
            "开始时间": "选择开始时间",
            "结束时间": "选择结束时间",
            "促销价格": "输入促销价格"
        }
        placeholder = placeholder_map.get(field_name)
        if not placeholder:
            raise ValueError(f"不支持的字段名: {field_name}")

        input_locator = (By.XPATH, f"//input[@placeholder='{placeholder}']")
        input_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(input_locator)
        )
        input_elem.clear()
        input_elem.send_keys(value)
        # 输入后点击 body 使日期输入生效（可选）
        if "时间" in field_name:
            self.driver.find_element(By.TAG_NAME, "body").click()

    def net_btn(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.NET_BTN)).click()




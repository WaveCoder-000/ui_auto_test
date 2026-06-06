from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class Step2BasicInfo(BasePage):
    from path.product.add_product import (GIFT_POINT,GIFT_GROWTH,GIFT_BUY,DETAIL_TITLE,
                                          DETAIL_DESCRIPTION,PRO_KEY, PRO_NOTE,NET_BTN2 )

    def fill_base_info(self, data: dict):
        # 赠送积分
        if "gift_point" in data:
            self.add_fill_input(self.GIFT_POINT, data["gift_point"])
        # 赠送成长值
        if "gift_growth" in data:
            self.add_fill_input(self.GIFT_GROWTH, data["gift_growth"])
        # 积分购买限制
        if "gift_buy" in data:
            self.add_fill_input(self.GIFT_BUY, data["gift_buy"])
        # 详细页标题
        if "detail_title" in data:
            self.add_fill_input(self.DETAIL_TITLE, data["detail_title"])
        # 详细页描述
        if "detail_description" in data:
            self.add_fill_input(self.DETAIL_DESCRIPTION, data["detail_description"])
        # 商品关键字
        if "pro_key" in data:
            self.add_fill_input(self.PRO_KEY, data["pro_key"])
        # 商品备注
        if "pro_note" in data:
            self.add_fill_input(self.PRO_NOTE, data["pro_note"])

    def set_switch_by_label(self, label: str, turn_on: bool):
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
        self.click_element(self.NET_BTN2)




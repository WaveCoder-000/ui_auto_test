from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class Step3BasicInfo(BasePage):

    SELECT_PRO=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[1]/div/div")
    # ---------- 颜色输入与增加 ----------
    COLOR_INPUT = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/input")
    ADD_COLOR_BTN = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[2]/div[2]/div[1]/div/div[1]/div/button/span")
    DELETE_COLOR=(By.XPATH,"")

    def select_attribute_type(self, option_text: str):
        """选择属性类型的下拉选项"""
        # 1. 点击属性类型对应的下拉框
        trigger = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SELECT_PRO)
        )
        trigger.click()
        # 2. 选择目标选项
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        f"//li[contains(@class,'el-select-dropdown__item') and .//span[text()='{option_text}']]"))
        )
        option.click()

    # ===================== 【正确】尺码复选框 核心方法 =====================


    # ---------- 尺码复选框（动态定位） ----------
    def _get_size_checkbox_locator(self, size_value: str):
        # 直接查找文本为 size_value（如'30'）的复选框 label，不依赖“尺码”文字
        return By.XPATH, f"//label[contains(@class,'el-checkbox') and .//span[@class='el-checkbox__label' and text()='{size_value}']]"

    def _clear_all_selected_sizes(self):
        """
        只清除【尺码】区域内已选中的复选框，不会碰颜色
        """
        # 1. 先找到“尺码：”后面那个 el-checkbox-group
        size_group_loc = (
            By.XPATH,
            "//div[contains(text(),'尺码')]/div[@class='el-checkbox-group']"
        )
        size_group = self.driver.find_element(*size_group_loc)

        # 2. 只在这个 group 里找已勾选的
        selected_elements = size_group.find_elements(
            By.XPATH,
            ".//label[contains(@class,'el-checkbox') and contains(@class,'is-checked')]"
        )

        for elem in selected_elements:
            try:
                elem.click()
            except:
                self.driver.execute_script("arguments[0].click();", elem)
            # 触发 change，让 Vue 更新
            self.driver.execute_script("""
                let input = arguments[0].querySelector('input');
                if(input) input.dispatchEvent(new Event('change', {bubbles:true}));
            """, elem)
            time.sleep(0.2)

    # ---------- 刷新列表按钮 ----------
    REFRESH_LIST_BTN = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[2]/div[2]/button[1]/span")
    SYNC_PRICE_BTN = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[2]/div[2]/button[2]/span")
    SYNC_STOCK_BTN = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[2]/div[2]/button[3]/span")

    # ---------- 私有操作方法 ----------
    def _add_color(self, color_name: str):
        color_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.COLOR_INPUT)
        )
        color_input.clear()
        color_input.send_keys(color_name)
        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_COLOR_BTN)
        )
        add_btn.click()
        # 等待颜色复选框出现，确保已添加
        checkbox = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,
                                        f"//label[contains(@class,'el-checkbox') and .//span[@class='el-checkbox__label' and text()='{color_name}']]"))
        )
        checkbox.click()

    def _select_size(self, size_value: str):
        locator = self._get_size_checkbox_locator(size_value)
        check_elem = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        # 滚动到可见（避免被遮挡）
        self.driver.execute_script("arguments[0].scrollIntoView(true);", check_elem)
        time.sleep(0.3)
        # 如果未选中则点击
        if "is-checked" not in check_elem.get_attribute("class"):
            try:
                check_elem.click()
            except Exception:
                # 若普通点击失败，使用 JavaScript 点击
                self.driver.execute_script("arguments[0].click();", check_elem)


    def _refresh_list(self):
        # 点击“刷新列表”按钮
        refresh_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.REFRESH_LIST_BTN)
        )
        refresh_btn.click()

        # 等待确认弹框出现，并点击“确定”按钮
        confirm_btn = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div/div[3]/button[2]/span"))
        )
        confirm_btn.click()

        # 等待表格至少出现一行数据（刷新完成）
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//table[contains(@class, 'el-table__body')]//tr[contains(@class, 'el-table__row')]"))
        )

    def _fill_sku_row(self, color: str, size: str, sale_price: str, promotion_price: str,
                      stock: str, stock_warning: str, sku_code: str):
        print(f">>> 填写SKU行: 颜色={color}, 尺码={size}")
        # 定位目标行：颜色在第一列，尺码在第二列
        row_xpath = f"//table[contains(@class,'el-table__body')]//tr[.//td[contains(., '{color}')] and .//td[contains(., '{size}')]]"
        row = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, row_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", row)
        time.sleep(0.5)

        # 销售价格（第3列）
        sale_input = row.find_element(By.XPATH, ".//td[3]//input")
        sale_input.clear()
        sale_input.send_keys(sale_price)

        # 促销价格（第4列）
        promo_input = row.find_element(By.XPATH, ".//td[4]//input")
        promo_input.clear()
        promo_input.send_keys(promotion_price)

        # 商品库存（第5列）
        stock_input = row.find_element(By.XPATH, ".//td[5]//input")
        stock_input.clear()
        stock_input.send_keys(stock)

        # 库存预警值（第6列）
        warning_input = row.find_element(By.XPATH, ".//td[6]//input")
        warning_input.clear()
        warning_input.send_keys(stock_warning)

        # SKU编号（第7列）
        sku_input = row.find_element(By.XPATH, ".//td[7]//input")
        sku_input.clear()
        sku_input.send_keys(sku_code)
        print("  SKU行填写完成")

    def _sync_price(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SYNC_PRICE_BTN)
        )
        btn.click()

        # 等待确认弹框出现，并点击“确定”按钮
        confirm_btn = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div/div[3]/button[2]/span"))
        )
        confirm_btn.click()

    def _sync_stock(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SYNC_STOCK_BTN)
        )
        btn.click()
        # 等待确认弹框出现，并点击“确定”按钮
        confirm_btn = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div/div[3]/button[2]/span"))
        )
        confirm_btn.click()

    def upload_attribute_image(self, image_path: str,image_path1:str):
        """上传属性图片"""
        # 定位 file input
        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[3]/div[2]/div/div/div/div/div[1]/div[1]/button"))
        )
        file_input2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[5]/div[2]/div/div[1]/ul/div/input"))
        )
        # 发送文件路径
        file_input.send_keys(image_path)
        file_input2.send_keys(image_path1)

    def select_param_by_label(self, label_text: str, option_text: str):
        print(f"正在选择 {label_text} -> {option_text}")
        label_xpath = f"//div[contains(@class,'paramInputLabel') and contains(text(),'{label_text}')]"
        label_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, label_xpath))
        )
        # 滚动到标签元素，使其位于视口中央
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", label_elem)
        time.sleep(0.5)
        # 找到下拉框触发区域并点击
        trigger = label_elem.find_element(By.XPATH,
                                          "./following-sibling::div[contains(@class,'el-select')]//div[contains(@class,'el-select__wrapper')]")
        trigger.click()
        # 等待下拉选项出现
        option_xpath = f"//div[contains(@class,'el-select-dropdown')]//li[contains(@class,'el-select-dropdown__item') and contains(.,'{option_text}')]"
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        )
        option.click()

    def set_product_detail_simple(self, detail_text: str, is_pc: bool = True):
        """通过切换iframe + 触发事件的方式，确保内容写入并显示"""
        pane_id = "pane-pc" if is_pc else "pane-mobile"
        tab_text = "电脑端详情" if is_pc else "移动端详情"

        # 1. 先点击选项卡，确保编辑器处于激活状态
        tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//*[text()='{tab_text}']"))
        )
        tab.click()
        # 等待选项卡切换完成
        time.sleep(0.3)
        # 2. 等待iframe出现并切换进去
        iframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"#{pane_id} iframe"))
        )
        self.driver.switch_to.frame(iframe)

        # 3. 等待body加载，写入内容并触发所有必要事件
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        self.driver.execute_script("""
            // 写入内容
            document.body.innerHTML = arguments[0];
            // 强制编辑器重绘
            document.body.focus();
            // 触发编辑器监听的所有事件，模拟用户输入
            document.body.dispatchEvent(new Event('input', {bubbles: true}));
            document.body.dispatchEvent(new Event('keyup', {bubbles: true}));
            document.body.dispatchEvent(new Event('change', {bubbles: true}));
            document.body.dispatchEvent(new Event('blur', {bubbles: true}));
        """, detail_text)

        # 4. 切回主文档
        self.driver.switch_to.default_content()
        time.sleep(0.5)

    NET_BTN=(By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[7]/div/div/button[2]")
    def net_btn(self):
        wait = WebDriverWait(self.driver, 10)
        net_btn = wait.until(EC.element_to_be_clickable(self.NET_BTN))
        net_btn.click()

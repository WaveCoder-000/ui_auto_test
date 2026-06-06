from selenium.webdriver.common.by import By

#搜索，删除
SEARCH_PRO_PATH = (By.XPATH,"//label[text()='输入搜索：']/following-sibling::div//input")
PRO_NUMBER_PATH = (By.XPATH,"//label[text()='商品货号：']/following-sibling::div//input")
SEARCH_BTN = (By.XPATH, "//span[text()=' 查询结果 ']/ancestor::button")
DELETE_BTN = (By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[11]/div/p[2]/button[2]")
RESET_BTN = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div[1]/div/div[1]/button[2]")
UP_STATUS_PATH = (By.XPATH, "//label[text()='上架状态：']/following-sibling::div//span[contains(text(), '全部')]")
REVIEW_STATUS_PATH = (By.XPATH,"//label[text()='审核状态：']/following-sibling::div//span[contains(text(), '全部')]")
PRO_SORT_PATH = (By.XPATH, "//label[text()='商品分类：']/following-sibling::div//input[@placeholder='请选择']")
TRIGGER_PATH = (By.XPATH, "//label[text()='商品品牌：']/following-sibling::div//span[contains(text(), '请选择')]")

#商品目录
PRODUCT = (By.XPATH, "//span[text()='商品']")
PRODUCT_LIST = (By.XPATH, "//li[contains(@class, 'el-menu-item')]//span[text()='商品列表']")
ADD_PRODUCT = (By.XPATH, "//li[contains(@class, 'el-menu-item')]//span[text()='添加商品']")
PRODUCT_SORT = (By.XPATH, "//li[contains(@class, 'el-menu-item')]//span[text()='商品分类']")
PRODUCT_STYLE = (By.XPATH, "//li[contains(@class, 'el-menu-item')]//span[text()='商品类型']")
BRAND_MANAGE = (By.XPATH, "//li[contains(@class, 'el-menu-item')]//span[text()='品牌管理']")

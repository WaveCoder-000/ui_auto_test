from selenium.webdriver.common.by import By

#添加商品页面1
CATEGORY_INPUT = (By.XPATH,"//label[text()='商品分类：']/following-sibling::div//input")
PRODUCT_NAME = (By.XPATH, "//label[text()='商品名称：']/following-sibling::div//input")
TITLE = (By.XPATH, "//label[text()='副标题：']/following-sibling::div//input")
PRODUCT_BRAND = (By.XPATH, "//label[text()='商品品牌：']/following-sibling::div//span")
PRO_INTRODUCE = (By.XPATH, "//label[text()='商品介绍：']/following-sibling::div//textarea")
PRO_NUMBER = (By.XPATH, "//label[text()='商品货号：']/following-sibling::div//input")
PRO_PRICE = (By.XPATH, "//label[text()='商品售价：']/following-sibling::div//input")
MARKET_PRICE = (By.XPATH, "//label[text()='市场价：']/following-sibling::div//input")
PRO_STOCK = (By.XPATH, "//label[text()='商品库存：']/following-sibling::div//input")
CALCULATE = (By.XPATH, "//label[text()='计量单位：']/following-sibling::div//input")
PRO_WEIGHT = (By.XPATH, "//label[text()='商品重量：']/following-sibling::div//input")
SORT = (By.XPATH, "//label[text()='排序']/following-sibling::div//input")
NET_BTN1 = (By.XPATH, "//button/span[text()='下一步，填写商品促销']")

#添加商品页面2
GIFT_POINT = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[1]/div/div/div/input")
GIFT_GROWTH = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[2]/div/div/div/input")
GIFT_BUY = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[3]/div/div/div/input")
DETAIL_TITLE = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[8]/div/div/div/input")
DETAIL_DESCRIPTION = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[9]/div/div/div/input")
PRO_KEY = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[10]/div/div/div/input")
PRO_NOTE = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[3]/form/div[11]/div/div/textarea")
NET_BTN2 = (By.XPATH, "//button/span[text()='下一步，填写商品属性']")

#添加商品页面3
SELECT_PRO = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[1]/div/div")
COLOR_INPUT = (By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/input")
ADD_COLOR_BTN = (By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[2]/div[2]/div[1]/div/div[1]/div/button/span")
REFRESH_LIST_BTN = (By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[2]/div[2]/button[1]/span")
SYNC_PRICE_BTN = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[2]/div[2]/button[2]/span")
SYNC_STOCK_BTN = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[2]/div[2]/button[3]/span")
NET_BTN3 = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[4]/form/div[7]/div/div/button[2]")
TIP_BTN_PATH = (By.XPATH, "/html/body/div[7]/div/div/div[3]/button[2]/span")

#添加商品页面4
TOPIC_CHECKBOX = (By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[5]/form/div[1]/div[2]/div/div[1]/div/div[1]/div/input")
MOVE_RIGHT_BTN = (By.XPATH, "//div[contains(@class,'el-transfer')]//button[contains(@class,'el-transfer__button')][2]")
NET_BTN = (By.XPATH, "/html/body/div[1]/div/div/div[2]/section/div/div/div[5]/form/div[3]/div/div/button[2]")
RIGHT_CHECKBOX_PATH = (By.XPATH,"/html/body/div[1]/div/div/div[2]/section/div/div/div[5]/form/div[1]/div[2]/div/div[3]/p/label")
CONFIRM_BTN = (By.XPATH, "/html/body/div[7]/div/div/div[3]/button[2]")
RIGHT_BTN_PATH = (By.CSS_SELECTOR, ".el-transfer__buttons button:last-child")


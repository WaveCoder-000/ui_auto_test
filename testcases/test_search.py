from time import time

import allure
import pytest
from faker import Faker

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.add_product.step2_promotion import Step2BasicInfo
from pages.add_product.step3_attributes import Step3BasicInfo
from pages.product_search_and_delete import SearchAndDelete
from pages.add_product.step4_relation import Step4BasicInfo
# from pages.product_search_and_delete import ProductListPage
# from pages.add_product_page import AddProductPage
from pages.edit_product_page import EditProductPage
from pages.side_common_btn import CommonPage
from config.settings import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.add_product.step1_basic_info import Step1BasicInfo
from selenium.webdriver.common.by import By
import time

fake = Faker(locale="zh_CN")

@allure.feature("商品管理")
@allure.story("CRUD闭环测试")
class TestProductCRUD:

    @allure.title("商品新增-查询-修改-删除完整闭环")
    def test_product_crud_cycle(self, driver,logger):
        logger.info("开始执行登录测试")
        login_page = LoginPage(driver)
        login_page.goto_login_page()
        login_page.login(USERNAME, PASSWORD)
        time.sleep(1)
        assert login_page.is_login_success(), "登录失败，未检测到后台主页元素"
        logger.info("登录测试通过")
        logger.info("开始执行点击商品列表测试")
        common = CommonPage(driver)
        common.product()
        # 查询
        common.product_list()
        search = SearchAndDelete(driver)
        print("点击了商品")
        search_data = {
            "product_name": "耐克NIKE 男子 气垫 休闲鞋 AIR MAX 90 ESSENTIAL 运动鞋 AJ1285-101白色41码",
            "product_number": "6799345"
        }
        print("输入完成")

        search.search_info(search_data)
        data=['服装','外套']
        search.select_category(data)
        search.select_brand("小米")
        search.up_status('上架')
        # search.review_status('未审核') # 有问题
        search.search_btn()
        search.delete_btn()
        search.reset_btn()
        search.search_info(search_data)
        search.search_btn()
        search.reset_btn()
        time.sleep(20)
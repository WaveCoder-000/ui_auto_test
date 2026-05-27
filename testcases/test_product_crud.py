from time import time

import allure
import pytest
from faker import Faker

from pages.add_product.step2_promotion import Step2BasicInfo
from pages.add_product.step3_attributes import Step3BasicInfo
from pages.product_search_and_delete import SearchAndDelete
from pages.add_product.step4_relation import Step4BasicInfo
# from pages.product_search_and_delete import ProductListPage
# from pages.add_product_page import AddProductPage
from pages.edit_product_page import EditProductPage
from pages.common_btn import CommonPage
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
        time.sleep(2)
        common=CommonPage(driver)
        common.product()
        common.add_product()
        logger.info("click测试通过")

        step1 = Step1BasicInfo(driver)
        category_path = ['服装', 'T恤']  # 根据实际可用的二级分类名调整
        step1.select_category(category_path)

        brand_path = ['小米']  # 根据实际可用的二级分类名调整
        step1.select_brand(brand_path)

        # 2. 填写其他基本信息（使用 fill_base_info 方法）
        product_data = {
            "product_name":  f"自动化测试商品_{fake.random_number(digits=6)}",
            "subtitle": "高品质自动测试副标题",
            "product_introduce": "这是商品介绍内容",  # 如果有富文本编辑器可能需要特殊处理，可先留空或简化
            "product_number": fake.ean13(),  # 生成13位随机商品货号
            "price": "199",
            "market_price": "299",
            "stock": "100",
            "unit": "件",
            "weight": "0.5",
            "sort": "0"
        }
        step1.fill_base_info(product_data)
        print("新增的数据",product_data.get("product_name"),product_data.get("product_number"))
        step1.net_btn()


    #第二页面
        step2 = Step2BasicInfo(driver)
        product_promotion_data = {
            "gift_point": "90",
            "gift_growth": "88",
            "gift_buy": "12",  # 如果有富文本编辑器可能需要特殊处理，可先留空或简化
            "detail_title": "新活动",  # 生成13位随机商品货号
            "detail_description": "新活动",
            "pro_key": "新",
            "pro_note": "新活动"
        }
        step2.fill_base_info(product_promotion_data)

        # 操作开关
        step2.set_switch_by_label("预告商品", True)
        step2.set_switch_by_label("商品上架", True)
        step2.set_switch_by_label("新品", True)
        step2.set_switch_by_label("推荐", False)

        # 复选框
        step2.set_service_checkbox("无忧退货", True)  # 勾选
        step2.set_service_checkbox("快速退款", True)
        step2.set_service_checkbox("免费包邮", False)  # 取消勾选
        step2.select_promotion_type("特惠促销")

        step2.set_field("开始时间", "2026-06-01 00:00:00")
        step2.set_field("结束时间", "2026-06-30 23:59:59")
        step2.set_field("促销价格", "299.00")
        step2.net_btn()

        # 第三页
        step3 = Step3BasicInfo(driver)
        step3.select_attribute_type("服装-裤装")
        step3._add_color("白色")
        step3._select_size("30")
        time.sleep(1)   # <--- 加这一行，等SKU行渲染出来
        step3._refresh_list()
        time.sleep(0.5) # <--- 再加这一行，保险
        step3._fill_sku_row("白色", "30", "100", "123", "10", "5", "12345")
        # step3._sync_price()
        # step3._sync_stock()
        #上传图片
        step3.upload_attribute_image(r"C:\Users\16353\Pictures\900f3e6387d0bb9363bb381019513b1f.jpg",r"C:\Users\16353\Pictures\900f3e6387d0bb9363bb381019513b1f.jpg")
        print("上传成功")
        # 在第四步页面中调用
        step3.select_param_by_label("适用人群:", "老年")
        step3.select_param_by_label("风格:", "嘻哈风格")
        step3.select_param_by_label("适用场景:", "运动")
        step3.select_param_by_label("上市时间:", "2018年春")

        step3.set_product_detail_simple("<p>终于成功了！！！！</p>", is_pc=True)
        step3.net_btn()


        #跳转成功
        #第四个页面
        step4 = Step4BasicInfo(driver)
        step4.move_topic_to_right("大牌手机低价秒")
        step4.select_all_right(True)
        time.sleep(5)
        step4.complete_btn()
        time.sleep(2)

        # 查询
        common.product_list()
        search = SearchAndDelete(driver)
        print("点击了商品")
        search_data = {
            "product_name": product_data.get("product_name"),
            "product_number": product_data.get("product_number"),
        }
        print("新增的数据",search_data.get("product_name"),search_data.get("product_number"))
        print("输入完成")
        search.search_info(search_data)
        data = ['服装', '外套']
        search.select_category(data)
        search.select_brand("小米")
        search.up_status('上架')
        # search.review_status('未审核') # 有问题
        search.search_btn()

        search.reset_btn()
        search = SearchAndDelete(driver)
        print("点击了商品")
        search_data = {
            "product_name": product_data.get("product_name"),
            "product_number": product_data.get("product_number"),
        }

        print("搜索的数据",search_data.get("product_name"),search_data.get("product_number"))
        print("输入完成")
        search.search_info(search_data)
        search.search_btn()
        edit = EditProductPage(driver)
        edit.edit_btn()
        # 编辑内容
        # 第一页
        step1 = Step1BasicInfo(driver)
        category_path = ['手机数码', '手机通讯']  # 根据实际可用的二级分类名调整
        step1.select_category(category_path)
        brand_path = ['苹果']  # 根据实际可用的二级分类名调整
        step1.select_brand(brand_path)

        # 2. 填写其他基本信息（使用 fill_base_info 方法）

        edit_product_data = {
            "product_name": f"自动化测试商品_{fake.random_number(digits=6)}",
            # "product_name": "8888",
            "subtitle": "高品质自动测试副标题",
            "product_introduce": "这是商品介绍内容",  # 如果有富文本编辑器可能需要特殊处理，可先留空或简化
            "product_number": fake.ean13(),  # 生成13位随机商品货号
            # "product_number": "8888",  # 生成13位随机商品货号
            "price": "199",
            "market_price": "299",
            "stock": "100",
            "unit": "件",
            "weight": "1",
            "sort": "0"
        }
        step1.fill_base_info(edit_product_data)

        print("编辑的数据",edit_product_data.get("product_name"),edit_product_data.get("product_number"))
        step1.net_btn()

        # 第二页
        step2 = Step2BasicInfo(driver)
        product_promotion_data = {
            "gift_point": "8812",
            "gift_growth": "123",
            "gift_buy": "12",  # 如果有富文本编辑器可能需要特殊处理，可先留空或简化
            "detail_title": "新活动",  # 生成13位随机商品货号
            "detail_description": "新活动",
            "pro_key": "新",
            "pro_note": "新活动"
        }
        step2.fill_base_info(product_promotion_data)

        # 操作开关
        step2.set_switch_by_label("预告商品", True)
        step2.set_switch_by_label("商品上架", False)
        step2.set_switch_by_label("新品", False)
        step2.set_switch_by_label("推荐", False)

        # 复选框
        step2.set_service_checkbox("无忧退货", False)  # 勾选
        step2.set_service_checkbox("快速退款", True)
        step2.set_service_checkbox("免费包邮", False)  # 取消勾选
        step2.select_promotion_type("特惠促销")

        step2.set_field("开始时间", "2026-06-01 00:00:00")
        step2.set_field("结束时间", "2026-06-30 23:59:59")
        step2.set_field("促销价格", "299.00")
        step2.net_btn()
        time.sleep(4)

        # 第三页
        step3 = Step3BasicInfo(driver)
        step3.select_attribute_type("服装-裤装")
        # step3.delete_color('白色')
        step3._add_color("金色")
        step3._clear_all_selected_sizes()
        step3._select_size("29")
        step3._refresh_list()
        # step3._fill_sku_row("白色", "30", "100", "123", "10", "5", "12345")
        step3._fill_sku_row("金色", "29", "100", "123", "10", "5", "12345")
        # step3._sync_price()
        # step3._sync_stock()
        # 上传图片
        step3.upload_attribute_image(r"C:\Users\16353\Pictures\900f3e6387d0bb9363bb381019513b1f.jpg",
                                     r"C:\Users\16353\Pictures\900f3e6387d0bb9363bb381019513b1f.jpg")
        print("上传成功")
        # 在第四步页面中调用
        step3.select_param_by_label("适用人群:", "中年")
        step3.select_param_by_label("风格:", "嘻哈风格")
        step3.select_param_by_label("适用场景:", "运动")
        step3.select_param_by_label("上市时间:", "2018年春")

        step3.set_product_detail_simple("<p>电脑端详情</p>", is_pc=True)
        step3.net_btn()

        step4 = Step4BasicInfo(driver)
        step4.move_topic_to_right("夏天应该穿什么")
        step4.complete_btn()

        edit_data = {
            "product_name": edit_product_data.get("product_name"),
            "product_number": edit_product_data.get("product_number"),
            # "product_name":"8888",
            # "product_number": "8888",
        }

        print("编辑的数据",edit_data.get("product_name"),edit_data.get("product_number"))
        # time.sleep(30)
        search.search_info(edit_product_data)
        search.search_btn()
        search.delete_btn()
        search.reset_btn()
        time.sleep(5)













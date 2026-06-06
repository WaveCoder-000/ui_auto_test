from time import time
import os
import allure
from faker import Faker
from pages.add_product.step2_promotion import Step2BasicInfo
from pages.add_product.step3_attributes import Step3BasicInfo
from pages.product_search_and_delete import SearchAndDelete
from pages.add_product.step4_relation import Step4BasicInfo
from pages.edit_product_page import EditProductPage
from pages.side_common_btn import CommonPage
from config.settings import USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.add_product.step1_basic_info import Step1BasicInfo
import time

fake = Faker(locale="zh_CN")

@allure.feature("商品管理")
@allure.story("CRUD闭环测试")
class TestProductCRUD:

    @allure.title("商品新增-查询-修改-删除完整闭环")
    def test_product_crud_cycle(self, driver, logger):
        current_dir = os.path.dirname(__file__)
        image_path = os.path.abspath(os.path.join(current_dir, "..", "data", "900f3e6387d0bb9363bb381019513b1f.jpg"))

        # ========== 登录 ==========
        logger.info("开始执行登录测试")
        login_page = LoginPage(driver)
        login_page.goto_login_page()
        login_page.login(USERNAME, PASSWORD)
        time.sleep(1)
        assert login_page.is_login_success(), "登录失败，未检测到后台主页元素"
        logger.info("登录测试通过")

        # ========== 进入添加商品页面 ==========
        logger.info("进入商品列表并点击添加商品")
        time.sleep(2)
        common = CommonPage(driver)
        common.product()
        common.add_product()
        logger.info("已进入添加商品页面")

        # ========== 第一步：填写基本信息 ==========
        logger.info("开始填写商品基本信息（第一步）")
        step1 = Step1BasicInfo(driver)

        category_path = ['服装', 'T恤']
        logger.info(f"选择分类: {category_path}")
        step1.select_category(category_path)

        brand_path = ['小米']
        logger.info(f"选择品牌: {brand_path}")
        step1.select_brand(brand_path)

        product_data = {
            "product_name": f"自动化测试商品_{fake.random_number(digits=6)}",
            "subtitle": "高品质自动测试副标题",
            "product_introduce": "这是商品介绍内容",
            "product_number": fake.ean13(),
            "price": "199",
            "market_price": "299",
            "stock": "100",
            "unit": "件",
            "weight": "0.5",
            "sort": "0"
        }
        step1.fill_base_info(product_data)
        logger.info(f"新增商品: 名称={product_data['product_name']}, 货号={product_data['product_number']}")

        step1.net_btn()  # 下一步

        # ========== 第二步：填写促销信息 ==========
        logger.info("开始填写促销信息（第二步）")
        step2 = Step2BasicInfo(driver)

        product_promotion_data = {
            "gift_point": "90",
            "gift_growth": "88",
            "gift_buy": "12",
            "detail_title": "新活动",
            "detail_description": "新活动",
            "pro_key": "新",
            "pro_note": "新活动"
        }
        step2.fill_base_info(product_promotion_data)

        step2.set_switch_by_label("预告商品", True)
        step2.set_switch_by_label("商品上架", True)
        step2.set_switch_by_label("新品", True)
        step2.set_switch_by_label("推荐", False)

        step2.set_service_checkbox("无忧退货", True)
        step2.set_service_checkbox("快速退款", True)
        step2.set_service_checkbox("免费包邮", False)

        step2.select_promotion_type("特惠促销")

        step2.set_field("开始时间", "2026-06-01 00:00:00")
        step2.set_field("结束时间", "2026-06-30 23:59:59")
        step2.set_field("促销价格", "299.00")

        step2.net_btn()  # 下一步

        # ========== 第三步：填写商品属性、SKU、详情等 ==========
        logger.info("开始填写商品属性和SKU（第三步）")
        step3 = Step3BasicInfo(driver)

        step3.select_attribute_type("服装-裤装")
        step3._add_color("白色")
        step3._select_size("30")
        time.sleep(2)
        step3._refresh_list()
        time.sleep(0.5)

        step3._fill_sku_row("白色", "30", "100", "123", "10", "5", "12345")
        time.sleep(3)

        step3._sync_price()
        step3._sync_stock()

        logger.info("上传商品相册图片")
        step3.upload_attribute_image(image_path, image_path)

        step3.select_param_by_label("适用人群:", "老年")
        step3.select_param_by_label("风格:", "嘻哈风格")
        step3.select_param_by_label("适用场景:", "运动")
        step3.select_param_by_label("上市时间:", "2018年春")

        step3.set_product_detail_simple("<p>终于成功了！！！！</p>", is_pc=True)

        step3.net_btn()  # 下一步

        # ========== 第四步：关联专题并提交 ==========
        logger.info("开始填写关联信息并提交（第四步）")
        step4 = Step4BasicInfo(driver)

        topic_name = "大牌手机低价秒"
        logger.info(f"移动专题: {topic_name}")
        step4.move_topic(topic_name)
        step4.right_btn()
        step4.select_all_right(True)
        time.sleep(3)
        step4.complete_btn()
        logger.info("商品新增提交完成")

        # ========== 查询验证新增商品 ==========
        logger.info("开始查询新增商品")
        common.product_list()
        search = SearchAndDelete(driver)

        search_data = {
            "product_name": product_data["product_name"],
            "product_number": product_data["product_number"],
        }
        logger.info(f"查询条件: 名称={search_data['product_name']}, 货号={search_data['product_number']}")
        search.search_info(search_data)

        search.select_category(['服装', 'T恤'])
        search.select_brand("小米")
        search.up_status('上架')
        search.search_btn()
        logger.info("查询完成")

        # 获取搜索结果并打印
        results = search.get_search_results()
        print("搜索到的数据：", results)
        assert len(results) > 0, f"未搜索到任何商品，条件：{search_data}"
        product_names = [item['name'] for item in results]
        product_numbers = [item['number'] for item in results]
        assert product_data["product_name"] in product_names, \
            f"新增商品名称 '{product_data['product_name']}' 未出现在搜索结果中，实际搜索到的名称：{product_names}"
        assert product_data["product_number"] in product_numbers, \
            f"新增货号 '{product_data['product_number']}' 未出现在搜索结果中，实际搜索到的货号：{product_numbers}"
        logger.info("查询验证新增商品断言通过（商品名称和货号均已确认）")
        search.reset_btn()

        # ========== 编辑商品 ==========
        logger.info("开始编辑商品")
        search.search_info(search_data)
        search.search_btn()
        edit = EditProductPage(driver)
        edit.edit_btn()
        logger.info("进入编辑页面")

        # 编辑-第一页
        logger.info("修改基本信息（第一页）")
        step1 = Step1BasicInfo(driver)

        step1.select_category(['手机数码', '手机通讯'])
        step1.select_brand(['苹果'])

        edit_product_data = {
            "product_name": f"自动化测试商品_{fake.random_number(digits=6)}",
            "subtitle": "高品质自动测试副标题",
            "product_introduce": "这是商品介绍内容",
            "product_number": fake.ean13(),
            "price": "199",
            "market_price": "299",
            "stock": "100",
            "unit": "件",
            "weight": "1",
            "sort": "0"
        }
        step1.fill_base_info(edit_product_data)
        logger.info(f"编辑后商品: 名称={edit_product_data['product_name']}, 货号={edit_product_data['product_number']}")
        step1.net_btn()

        # 编辑-第二页
        logger.info("修改促销信息（第二页）")
        step2 = Step2BasicInfo(driver)

        edit_promotion_data = {
            "gift_point": "8812",
            "gift_growth": "123",
            "gift_buy": "12",
            "detail_title": "新活动",
            "detail_description": "新活动",
            "pro_key": "新",
            "pro_note": "新活动"
        }
        step2.fill_base_info(edit_promotion_data)

        step2.set_switch_by_label("预告商品", True)
        step2.set_switch_by_label("商品上架", False)
        step2.set_switch_by_label("新品", False)
        step2.set_switch_by_label("推荐", False)

        step2.set_service_checkbox("无忧退货", False)
        step2.set_service_checkbox("快速退款", True)
        step2.set_service_checkbox("免费包邮", False)

        step2.select_promotion_type("特惠促销")

        step2.set_field("开始时间", "2026-06-01 00:00:00")
        step2.set_field("结束时间", "2026-06-30 23:59:59")
        step2.set_field("促销价格", "299.00")

        step2.net_btn()
        time.sleep(4)

        # 编辑-第三页
        logger.info("修改商品属性（第三页）")
        step3 = Step3BasicInfo(driver)

        step3.select_attribute_type("服装-裤装")
        step3._add_color("金色")
        step3._clear_all_selected_sizes()
        step3._select_size("29")
        step3._refresh_list()
        step3._fill_sku_row("金色", "29", "100", "123", "10", "5", "12345")
        step3._sync_price()
        step3._sync_stock()
        step3.upload_attribute_image(image_path, image_path)

        step3.select_param_by_label("适用人群:", "中年")
        step3.select_param_by_label("风格:", "嘻哈风格")
        step3.select_param_by_label("适用场景:", "运动")
        step3.select_param_by_label("上市时间:", "2018年春")

        step3.set_product_detail_simple("<p>电脑端详情</p>", is_pc=True)
        step3.net_btn()

        # 编辑-第四页
        logger.info("修改关联信息（第四步）")
        step4 = Step4BasicInfo(driver)

        new_topic = "夏天应该穿什么"
        logger.info(f"移动新专题: {new_topic}")
        step4.move_topic(new_topic)
        step4.right_btn()
        step4.select_all_right(True)
        time.sleep(3)
        step4.complete_btn()
        logger.info("商品编辑完成并保存")
        success_msg = step4.get_success_message()  # 需在 Step4BasicInfo 中实现该方法，例如获取 .el-message 文本
        print("编辑的成功信息："+success_msg)
        assert "提交成功" in success_msg or "添加成功" in success_msg, f"新增商品失败，页面提示：{success_msg}"
        logger.info("编辑商品断言通过") 

        # ========== 删除编辑后的商品 ==========
        logger.info("开始删除商品")
        edit_data = {
            "product_name": edit_product_data["product_name"],
            "product_number": edit_product_data["product_number"],
        }
        logger.info(f"删除条件: 名称={edit_data['product_name']}, 货号={edit_data['product_number']}")
        search.search_info(edit_data)
        search.search_btn()
        search.delete_btn()
        search.search_info(edit_data)
        results = search.get_search_results()
        print(f"删除后搜索结果：{results}")

        # 断言：搜索结果应为空，或者不包含该商品名称和货号
        assert len(results) == 0, f"删除后仍然搜索到 {len(results)} 条记录，商品未被彻底删除"
        logger.info("删除商品断言通过")
        search.reset_btn()
        time.sleep(1)
        logger.info("商品CRUD闭环测试全部执行完毕")
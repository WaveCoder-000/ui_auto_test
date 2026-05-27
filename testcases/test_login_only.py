import pytest
import time
from pages.login_page import LoginPage
from config.settings import USERNAME, PASSWORD

class TestAdminLogin:

    def test_login_success(self, driver, logger):
        """测试后台管理员正常登录"""
        logger.info("开始执行登录测试")
        login_page = LoginPage(driver)
        login_page.goto_login_page()
        login_page.login(USERNAME, PASSWORD)
        time.sleep(2)
        assert login_page.is_login_success(), "登录失败，未检测到后台主页元素"
        logger.info("登录测试通过")

    # 你可以继续添加更多测试，比如错误密码等
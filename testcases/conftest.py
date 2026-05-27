import pytest
from common.driver_manager import create_chrome_driver
from common.logger import setup_logger

@pytest.fixture(scope="function")
def driver():
    """每个测试用例启动一个新浏览器，结束自动关闭"""
    driver = create_chrome_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def logger():
    """会话级 logger，可在用例中记录日志"""
    return setup_logger()
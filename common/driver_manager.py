from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.settings import CHROME_DRIVER_PATH

def create_chrome_driver():
    """创建并返回 Chrome WebDriver 实例"""
    service = Service(executable_path=CHROME_DRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # 如果你需要无头模式，去掉下面注释
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    return driver
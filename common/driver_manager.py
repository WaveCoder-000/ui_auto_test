import platform  # 用于判断当前操作系统
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# --- 如果是 Windows 环境，需要从配置文件导入路径 ---
# 注意：这里假设你的 config/settings.py 里定义了 CHROME_DRIVER_PATH
# 如果运行报错说找不到 settings，说明路径不对，暂时先注释掉，用自动管理
try:
    from config.settings import CHROME_DRIVER_PATH
except ImportError:
    CHROME_DRIVER_PATH = None


def create_chrome_driver():
    """
    根据不同操作系统创建 Chrome 驱动
    - Linux: 使用固定的 /usr/local/chromedriver/chromedriver (用于服务器)
    - Windows: 使用 config.settings 里配置的路径 (用于本地开发)
    """

    # 1. 获取当前操作系统
    current_os = platform.system()

    # 2. 根据操作系统配置不同的 Service 和 Options
    if current_os == "Linux":
        print("🚀 检测到 Linux 环境，使用服务器固定路径...")

        # --- Linux 配置 (你的服务器环境) ---
        driver_path = '/usr/local/chromedriver/chromedriver'
        service = Service(executable_path=driver_path)

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    else:
        # --- Windows 配置 (你的本地开发环境) ---
        print("检测到 Windows 环境，使用配置文件路径...")

        # 这里使用你提到的“写在别的文件里的路径”
        if CHROME_DRIVER_PATH is None:
            raise Exception(
                "请在 config/settings.py 中配置 CHROME_DRIVER_PATH，或者在此处填入你的 chromedriver.exe 路径")

        service = Service(executable_path=CHROME_DRIVER_PATH)

        options = Options()
        options.add_argument("--start-maximized")  # 本地开发通常需要看界面
        # options.add_argument("--headless") # 如果想静默运行，取消注释这行

    # 3. 启动浏览器
    driver = webdriver.Chrome(service=service, options=options)
    return driver
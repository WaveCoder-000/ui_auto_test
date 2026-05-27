# 全局配置
BASE_URL = "http://localhost:5173"          # 你的基地址
LOGIN_PATH = "/login"                       # 登录页路径（请根据实际修改）
LOGIN_URL = BASE_URL + LOGIN_PATH

USERNAME = "admin"
PASSWORD = "macro123"

# Chrome 驱动绝对路径（你的路径）
CHROME_DRIVER_PATH = r"D:\gugedriver\chromedriver-win64\chromedriver.exe"

# 等待时间（秒）
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 10

# 截图配置
SCREENSHOT_DIR = "screenshots"

# 日志配置
LOG_LEVEL = "INFO"
LOG_DIR = "logs"
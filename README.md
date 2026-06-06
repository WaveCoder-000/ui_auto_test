# Mall 电商项目 UI 自动化测试

## 📖 项目简介
本项目是针对 GitHub 开源项目 [Mall (83.8k stars)](https://github.com/macrozheng/mall) 进行的 UI 自动化测试脚本。旨在验证商城核心业务流程的稳定性。

**被测系统源码：**
- 后端服务: [macrozheng/mall](https://github.com/macrozheng/mall)
- 前端页面: [macrozheng/mall-admin-web](https://github.com/macrozheng/mall-admin-web)

## 🛠️ 环境准备与部署
在运行测试前，请确保已在本地成功部署上述前后端项目。

1. **安装 Python 依赖**
   ```bash
   pip install -r requirements.txt
   
修改你在本地运行的谷歌浏览器的驱动地址，如果在linux运行的话页要修改一下驱动地址
修改文件在 common/driver_manager.py和config/settings.py

运行并生成报告
pytest testcases/test_product_crud.py --alluredir=./allure-results -v -s
清空已有的并打开
allure generate ./allure-results -o ./allure-report --clean
allure open ./allure-report

运行的allore报告在images下的照片

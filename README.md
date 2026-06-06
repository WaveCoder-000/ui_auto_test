运行并生成报告
pytest testcases/test_product_crud.py --alluredir=./allure-results -v -s
清空已有的并打开
allure generate ./allure-results -o ./allure-report --clean
allure open ./allure-report

运行的allore报告在images下的照片
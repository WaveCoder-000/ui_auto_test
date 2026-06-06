pipeline {
    agent any

    environment {
        // 【已修正】根据你的截图提示，前端运行在 5173 端口
        BASE_URL = "http://192.168.148.129:5173"
        USERNAME = "admin"
        PASSWORD = "macro123"
        CHROME_OPTIONS = "--headless --no-sandbox --disable-dev-shm-usage"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run UI Tests') {
            steps {
                sh '''
                    # 显式激活环境并导出变量
                    . venv/bin/activate
                    export BASE_URL=${BASE_URL}
                    export USERNAME=${USERNAME}
                    export PASSWORD=${PASSWORD}
                    export CHROME_OPTIONS=${CHROME_OPTIONS}

                    # 运行测试
                    pytest testcases/test_product_crud.py --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            // 1. 生成 Allure 报告
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]

            // 2. 发送邮件通知 (针对手机端优化的版本)
            script {
                // 获取当前构建状态，如果为空则默认为 SUCCESS
                def buildStatus = currentBuild.result ?: 'SUCCESS'

                // 动态设置邮件标题，方便手机通知栏直接查看
                def subject = "[${buildStatus}] 自动化测试报告 - ${env.JOB_NAME} #${env.BUILD_NUMBER}"

                // 定义邮件正文
                def body = """
                    <h2>🚀 自动化测试执行结果</h2>
                    <p><strong>构建状态:</strong> <span style="color:${buildStatus == 'SUCCESS' ? 'green' : 'red'}; font-size: 1.2em;">${buildStatus}</span></p>
                    <p><strong>项目名称:</strong> ${env.JOB_NAME}</p>
                    <p><strong>构建编号:</strong> #${env.BUILD_NUMBER}</p>
                    <hr/>
                    <p><a href="${env.BUILD_URL}allure">👉 点击查看详细 Allure 报告</a></p>
                    <p><a href="${env.BUILD_URL}console">📄 查看控制台日志</a></p>
                """

                // 发送邮件
                emailext (
                    to: '1635341450@qq.com', // 【请确认】这是你的接收邮箱
                    subject: subject,
                    body: body,
                    mimeType: 'text/html',      // 必须开启 HTML 格式
                    attachLog: true             // 可选：将日志作为附件发送，方便排查错误
                )
            }

            // 3. 清理工作空间
            // 排除 allure-results 目录，保留历史数据用于生成趋势图
            cleanWs(
                cleanWhenNotBuilt: false,
                patterns: [[pattern: 'allure-results/**', type: 'EXCLUDE']]
            )
        }
    }
}
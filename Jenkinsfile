pipeline {
    agent any

    environment {
        TZ = "Asia/Dubai"
    }

    stages {
        stage('Code Formatting') {
            steps {
                echo '🚀 بدء تنسيق الكود باستخدام Black'

                // تثبيت Black ودعم Jupyter
                sh 'pip install -q black "black[jupyter]" || true'

                // تنفيذ إعادة تنسيق تلقائي
                sh 'black . || echo "⚠️ بعض الملفات تم تنسيقها تلقائيًا"'

                // فحص التنسيق وإظهار تحذير فقط إذا فشل
                sh 'black --check . || echo "::warning file=streamlit_app.py::Black formatting needed"'
            }
        }

        stage('Build') {
            steps {
                echo '🔧 بدء مرحلة البناء أو تشغيل التطبيق'
                // أضف هنا أوامر التحليل أو التنفيذ الخاصة بك
            }
        }

        stage('Set Build Name') {
            steps {
                script {
                    def buildDate = new Date().format('dd-MM-yyyy')
                    buildName "📊 Budget Analyzer CI – Build #${BUILD_NUMBER} on ${buildDate}"
                }
            }
        }

        stage('Set Build Description') {
            steps {
                script {
                    def timeStamp = new Date().format('HH:mm dd-MM-yyyy')
                    buildDescription("✅ تم التنفيذ بنجاح عند ${timeStamp} (GMT+4)")
                }
            }
        }
    }

    post {
        success {
            echo "✅ تم تنفيذ الـ build بنجاح في ${new Date().format('HH:mm dd-MM-yyyy')}"
        }
        failure {
            echo "❌ فشل التنفيذ عند ${new Date().format('HH:mm dd-MM-yyyy')}"
        }
    }
}
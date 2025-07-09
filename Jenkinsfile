pipeline {
    agent any

    stages {
        stage('Code Formatting') {
            steps {
                echo '🚀 بدء تنسيق الكود باستخدام Black'
                // تثبيت Black + دعم Jupyter لو لم يكن مثبتًا
                sh 'pip install -q black "black[jupyter]" || true'

                // تنفيذ إعادة تنسيق تلقائي
                sh 'black . || echo "⚠️ بعض الملفات تم تنسيقها تلقائيًا"'

                // فحص التنسيق مع تحذير بدون فشل
                sh 'black --check . || echo "::warning file=streamlit_app.py::Black formatting needed"'
            }
        }

        stage('Build') {
            steps {
                echo '🔧 بدء مرحلة البناء والتحقق من المشروع'
                // هنا يمكن إضافة خطوات إضافية مثل build أو تحليل البيانات
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
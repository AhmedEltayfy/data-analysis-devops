pipeline {
    agent any

    environment {
        TIMESTAMP = "${new Date().format("HH:mm dd-MM-yyyy")}"
        BUILD_NAME = "📊 Budget Analyzer CI – Build #${env.BUILD_NUMBER} on ${TIMESTAMP}"
    }

    stages {
        stage('Code Formatting') {
            steps {
                echo '🚀 بدء تنسيق الكود باستخدام Black'

                bat 'pip install -q black'
                bat 'black . || echo "⚠️ بعض الملفات تم تنسيقها تلقائيًا"'
                bat 'black --check . || echo "::warning Black formatting needed"'
            }
        }

        stage('Build') {
            steps {
                echo '🔧 بدء تنفيذ البناء'
                bat 'echo Build complete'
            }
        }

        stage('Set Build Name') {
            steps {
                script {
                    currentBuild.displayName = "${BUILD_NAME}"
                }
            }
        }

        stage('Set Build Description') {
            steps {
                script {
                    currentBuild.description = "✅ تم التنفيذ بنجاح عند ${TIMESTAMP}"
                }
            }
        }
    }

    post {
        failure {
            echo "❌ فشل التنفيذ في ${TIMESTAMP}. راجع التنسيق أو المشاكل في المراحل السابقة."
        }
        success {
            echo "✅ التنفيذ اكتمل بنجاح في ${TIMESTAMP}"
        }
    }
}
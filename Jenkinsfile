pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo '🔧 Starting build...'
            }
        }

        stage('Set Build Name') {
            steps {
                buildName "📊 Budget CI – Build #${BUILD_NUMBER} on ${new Date().format('dd-MM-yyyy')}"
            }
        }
    }

    post {
        success {
            echo "✅ Build succeeded at ${new Date().format('HH:mm dd-MM-yyyy')}"
        }
        failure {
            echo "❌ Build failed at ${new Date().format('HH:mm dd-MM-yyyy')}"
        }
    }
}
pipeline {
    agent any
    stages {
        stage ("download code") {
            steps {
                sh 'git clone https://github.com:techbleat/containers101.git'
            }
        }
        stage ('build image') {
            steps {
                sh '''
                   cd containers101
                   docker build -t shegoj/marcifx:v5
                '''
            }
        }
    }
    post {
        always {
            deleteDir()
        }
    }
}
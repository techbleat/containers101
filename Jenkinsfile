pipeline {
    agent any
    environment {
        myuser  = credentials ('dockerhub-user')
        mypassword =  credentials ('dockerhub-password')
    }
    stages {
        stage ("download code") {
            steps {
                sh 'git clone https://github.com/techbleat/containers101.git'
            }
        }
        stage ('build image') {
            steps {
                sh '''
                   cd containers101
                   docker build -t shegoj/marcifx:v5 .
                '''
            }
        }
        stage ('publish image') {
            steps {
                sh '''
                   docker login -u $myuser -p $mypassword
                   docker push shegoj/marcifx:v5 
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
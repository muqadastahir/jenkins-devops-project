pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {

        stage('Code Fetch') {
            steps {
                checkout scm
            }
        }

        stage('Docker Cleanup') {
            steps {
                sh '''
                docker stop flask-container || true
                docker rm flask-container || true
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                docker build -t flask-cicd:v1 .
                '''
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                docker run -d --name flask-container -p 5000:5000 flask-cicd:v1
                '''
            }
        }
    }
}

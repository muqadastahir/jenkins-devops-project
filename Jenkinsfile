pipeline {
    agent any

    stages {

        stage('Code Fetch') {
            steps {
                git branch: 'main', url: 'https://github.com/muqadastahir/jenkins-devops-project.git'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t flask-cicd:v1 .'
            }
        }

        stage('Docker Run') {
            steps {
                sh 'docker run -d -p 5000:5000 flask-cicd:v1 || true'
            }
        }
    }
}

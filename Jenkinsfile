pipeline {
    agent any

    stages {

        stage('Code Fetch') {
            steps {
                sh 'rm -rf app'
                sh 'git clone https://github.com/muqadastahir/jenkins-devops-project.git app'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'cd app && docker build -t muqadasmt/flask-cicd:v1 .'
            }
        }

        stage('Docker Push') {
            steps {
                sh 'docker push muqadasmt/flask-cicd:v1'
            }
        }

        stage('Kubernetes Deployment') {
            steps {
                sh 'kubectl apply -f app/deployment.yaml --validate=false'
                sh 'kubectl apply -f app/service.yaml --validate=false'
            }
        }

        stage('Monitoring Verification') {
            steps {
                sh 'kubectl get pods -n monitoring'
            }
        }
    }
}

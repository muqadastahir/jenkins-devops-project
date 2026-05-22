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
stage('Kubernetes Deployment') {
    steps {
        sh '''
          kubectl apply -f deployment.yaml --validate=false
          kubectl apply -f service.yaml --validate=false
          kubectl apply -f servicemonitor.yaml --validate=false
        '''
    }
}
stage('Prometheus-Grafana Monitoring') {
            steps {
                sh '''
                kubectl get pods -n monitoring
                kubectl get servicemonitor
                '''
            }
        }

    }
}

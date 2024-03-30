pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Build your GUI application
            }
        }
        stage('Dockerize') {
            steps {
                // Build Docker image
            }
        }
        stage('Deploy') {
            steps {
                // Deploy to Minikube
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}

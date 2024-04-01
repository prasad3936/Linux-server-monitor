pipeline {
    agent any 
    
    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        
        stage('Checkout Source Code') {
            steps {
                git 'https://github.com/prasad3936/Linux-server-monitor'
            }
        }

        stage('Build Docker') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-cred') {
                        docker.build("praszp246/cicd-e2e:${IMAGE_TAG}", '.').push()
                    }
                }
            }
        }

        stage('Checkout K8S manifest SCM') {
            steps {
                git 'https://github.com/prasad3936/linux-monitor-manifest.git'
            }
        }

        stage('Update K8S manifest & push to Repo') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'github', variable: 'GITHUB_CREDENTIALS')]) {
                        sh '''
                        cat deploy.yaml
                        sed -i '' "s/32/${BUILD_NUMBER}/g" deploy.yaml
                        cat deploy.yaml
                        git add deploy.yaml
                        git commit -m 'Updated the deploy yaml | Jenkins Pipeline'
                        git push https://github.com/prasad3936/linux-monitor-manifest.git HEAD:main
                        '''
                    }
                }
            }
        }
    }
}
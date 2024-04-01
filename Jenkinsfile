pipeline {
    agent any 
    
    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/prasad3936/Linux-server-monitor.git'
            }
        }

        stage('Build Docker') {
            steps {
                script {
                    sh '''
                    echo 'Build Docker Image'
                    docker build -t praszp246/cicd-e2e:${BUILD_NUMBER} .
                    '''
                }
            }
        }

        stage('Push the artifacts') {
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
                git branch: 'main', url: 'https://github.com/prasad3936/linux-monitor-manifest.git'
            }
        }
        
        stage('Update K8S manifest & push to Repo') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'git', variable: 'GITHUB_TOKEN')]) {
                        sh '''
                        cat deploy.yml
                        sed -i "s/replaceImageTag/${BUILD_NUMBER}/g" deploy.yml
                        cat deploy.yml
                        git add deploy.yml
                        git commit -m 'Updated the deploy yaml | Jenkins Pipeline'
                        git remote -v
                        git push https://github.com/prasad3936/linux-monitor-manifest.git HEAD:main
                        '''                        
                    }
                }
            }
        }
    }
}

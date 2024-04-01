pipeline {
    
    agent any 
    
    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        
        stage('Checkout'){
           steps {
                git 'https://github.com/prasad3936/Linux-server-monitor'
           }
        }

        stage('Build Docker'){
            steps{
                script{
                    withCredentials([usernamePassword(credentialsId: 'docker-cred', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh '''
                        echo 'Push to Repo'
                        docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
                        docker push praszp246/cicd-e2e:${BUILD_NUMBER}
                        docker logout
                        '''
                }
            }
        }

        stage('Push the artifacts'){
           steps{
                script{
                     sh '''
                    echo 'Buid Docker Image'
                    docker build -t praszp246/cicd-e2e:${BUILD_NUMBER} .
                    '''
                }
            }
        }
        
        stage('Checkout K8S manifest SCM'){
            steps {
                git 'https://github.com/prasad3936/linux-monitor-manifest.git'
            }
        }
        
        stage('Update K8S manifest & push to Repo'){
            steps {
                script{
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
}

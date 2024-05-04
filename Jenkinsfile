pipeline {
    agent any 
    //To avoid clash in image build numbers and to make it easy to point out related image builds
    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    
    stages { //Checking the code is first step 
        stage('Checkout') {
            steps {
                git 'https://github.com/prasad3936/Linux-server-monitor.git'
            }
        }

        stage('Build Docker') { //Building the container image
            steps {
                script {
                    sh '''
                    echo 'Build Docker Image'
                    docker build -t praszp246/cicd-e2e:${BUILD_NUMBER} .
                    '''
                }
            }
        }

        stage('Push the artifacts') { //You have to push the image to a central repository , making it easy to access . Central Repository used here is Dockerhub
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-cred') {
                        docker.build("praszp246/cicd-e2e:${IMAGE_TAG}", '.').push()
                    }
                }
            }
        }
        
        stage('Checkout K8S manifest SCM') {//Checking Out Manifest files for k8s
            steps {
                git branch: 'main', url: 'https://github.com/prasad3936/linux-monitor-manifest.git'
            }
        }
        
        stage('Update K8S manifest & push to Repo') {
            steps { //This section is to update manifest files after every iteration of code update performed 
                script {
                    withCredentials([string(credentialsId: 'git-jen', variable: 'GITHUB_TOKEN')]) {
                        sh '''
                        cat deploy.yml
                        sed -i "s/replaceImageTag/${BUILD_NUMBER}/g" deploy.yml
                        cat deploy.yml
                        git add deploy.yml
                        cat pod.yml
                        sed -i "s/16/${BUILD_NUMBER}/g" pod.yml
                        cat pod.yml
                        git add pod.yml
                        git config user.email "prasadcpatil246@gmail.com" //login
                        git config user.name "prasad3936"
                        git status
                        git commit -m 'Updated the deploy yaml | Jenkins Pipeline'
                        git remote -v
                        git push https://${GITHUB_TOKEN}@github.com/prasad3936/linux-monitor-manifest HEAD:main
                        '''                        
                    }
                }
            }
        }
    }
}

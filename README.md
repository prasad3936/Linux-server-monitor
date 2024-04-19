Hi There ! ,Here are the step-by-step details to set up an end-to-end Jenkins pipeline for a flask application using SonarQube, Argo CD, Helm, and Kubernetes:

![cicd drawio](https://github.com/prasad3936/Linux-server-monitor/assets/63768420/81497be1-1570-4682-a10e-f0927c72b99e)


Prerequisites:

1. Application code hosted on a Git repository
2. Jenkins server
3. Kubernetes cluster
4. Argo CD

Steps:

1. Install the necessary Jenkins plugins:
   1.1 Git plugin
   1.2 Pipeline plugin
   1.3 Kubernetes Continuous Deploy plugin

2. Create a new Jenkins pipeline:
   2.1 In Jenkins, create a new pipeline job and configure it with the Git repository URL for the flask application.
   2.2 Add a Jenkinsfile to the Git repository to define the pipeline stages.

3. Define the pipeline stages:
    Stage 1: Checkout the source code from Git.
    Stage 2: Run SonarQube analysis to check the code quality.
    Stage 3 : Check for manifest files
    Stage 4 : Promote the application to a production environment using Argo CD.
    Stage 5 : Update manifest files and push to repository


6. Set up Argo CD:
    Install Argo CD on the Kubernetes cluster.
    Set up a Git repository for Argo CD to track the changes in the Helm charts and Kubernetes manifests.
    Add the Helm chart to the Git repository that Argo CD is tracking.

7. Configure Jenkins pipeline to integrate with Argo CD:
   6.1 Add the Argo CD API token to Jenkins credentials.
   6.2 Update the Jenkins pipeline to include the Argo CD deployment stage.

8. Run the Jenkins pipeline:
   7.1 Trigger the Jenkins pipeline to start the CI/CD process for the Java application.
   7.2 Monitor the pipeline stages and fix any issues that arise.

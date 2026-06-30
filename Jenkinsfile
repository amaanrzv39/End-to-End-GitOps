pipeline {
    agent any

    environment{
        GCP_PROJECT = "project-cd8d3620-549d-44e4-ba7"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }

    stages {
        stage('Checkout Github') {
            steps {
                echo 'Pull code from GitHub...'
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'GitHub-token', url: 'https://github.com/amaanrzv39/End-to-End-GitOps.git']])
			    }
        }

        stage('Build Docker Image and push to gcr') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script{
                        echo "Building and pushing docker image to gcr....."
                        sh '''
                        pwd
                        ls -la
                        find . -name "Dockerfile"
                        export PATH=$PATH:${GCLOUD_PATH}
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}
                        gcloud auth configure-docker --quiet
                        docker build -t gcr.io/${GCP_PROJECT}/smart-machines:latest .
                        docker push gcr.io/${GCP_PROJECT}/smart-machines:latest
                        '''
                    }
                }
            }
        }

        stage('Install Kubectl & ArgoCD CLI') {
            steps {
                echo 'Installing Kubectl and ArgoCD CLI...'
            }
        }

        stage('Apply Kubernetes & Sync App with ArgoCD') {
            steps {
                echo 'Applying Kubernetes and syncing with ArgoCD...'
            }
        }
    }
}

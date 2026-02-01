pipeline {
    agent any

    environment {
        IMAGE_NAME = 'ci-cd-flask-app'
        CONTAINER_NAME = 'ci-cd-flask-container'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/arifzaman1/ci-cd-pipeline-flask-app.git'
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'python3 test_app.py'
                }
            }
        }

        stage ('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        STAGE('Run Container') {
            steps {
                script {
                    // Stop any existing container
                    sh "docker rm -f ${CONTAINER_NAME} || true"
                    // Run new container
                    sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        faliure {
            echo 'Pipeline failed. Check logs!'
        }
    }
}
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sowmya959/simple-chat-app:latest"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/Sowmyairuku/casestudy.git',
                    credentialsId: 'github-token'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t %DOCKER_IMAGE% .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    bat '''
                        echo %PASS% | docker login -u %USER% --password-stdin
                        docker push %DOCKER_IMAGE%
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo '✅ CI/CD Pipeline executed successfully!'
        }
        failure {
            echo '❌ CI/CD Pipeline failed!'
        }
    }
}

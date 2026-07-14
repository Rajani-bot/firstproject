pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'git remote add origin https://github.com/Rajani-bot/firstproject.git'
            }
        }

        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Artifact') {
            steps {
                sh 'zip artifact.zip *.py requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-microservice:latest .'
            }
        }

    }

    post {

        success {
            mail to: 'abc@gmail.com',
            subject: 'Build Successful',
            body: 'Pipeline executed successfully.'
        }

        failure {
            mail to: 'abc@gmail.com',
            subject: 'Build Failed',
            body: 'Pipeline failed.'
        }
    }

}
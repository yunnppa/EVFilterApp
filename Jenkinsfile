pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                sh 'flake8 app'
            }
        }
        stage('Security (SAST & SCA)') {
            steps {
                sh 'bandit -r app'
                sh 'safety check'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests'
            }
        }
        stage('Run Flask App') {
            steps {
                sh 'python3 run.py'
            }
        }
    }
}

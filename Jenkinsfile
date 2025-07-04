pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'pip install flake8 && flake8 app'
            }
        }

        stage('Security (SAST & SCA)') {
            steps {
                sh 'pip install bandit safety && bandit -r app && safety check || true'
            }
        }

        stage('Test') {
            steps {
                sh 'pip install pytest && pytest tests'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'pip install -r requirements.txt && python run.py'
            }
        }
    }
}

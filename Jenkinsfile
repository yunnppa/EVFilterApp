pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'flake8 src'
            }
        }

        stage('Security (SAST & SCA)') {
            steps {
                sh 'bandit -r src'
                sh 'safety check'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest tests'
            }
        }

        stage('Run Application') {
            steps {
                sh 'python src/main.py'
            }
        }
    }
}

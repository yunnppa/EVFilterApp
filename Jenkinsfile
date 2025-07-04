pipeline {
    agent any

    stages {
        stage('Install Python') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'python3 -m pip install flake8 && flake8 app'
            }
        }

        stage('Security (SAST & SCA)') {
            steps {
                sh 'python3 -m pip install bandit safety && bandit -r app && safety check'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pip install pytest && pytest tests'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'python3 run.py'
            }
        }
    }
}

pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh './$VENV_DIR/bin/pip install --upgrade pip'
                sh './$VENV_DIR/bin/pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh './$VENV_DIR/bin/pip install flake8'
                sh './$VENV_DIR/bin/flake8 app'
            }
        }

        stage('Security (SAST & SCA)') {
            steps {
                sh './$VENV_DIR/bin/pip install bandit safety'
                sh './$VENV_DIR/bin/bandit -r app || true'
                sh './$VENV_DIR/bin/safety check || true'
            }
        }

        stage('Test') {
            steps {
                sh './$VENV_DIR/bin/pip install pytest'
                sh './$VENV_DIR/bin/pytest tests'
            }
        }

        stage('Run Flask App') {
            steps {
                sh './$VENV_DIR/bin/python run.py'
            }
        }
    }
}

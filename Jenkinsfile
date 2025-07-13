pipeline {
    agent any

    environment {
        VENV = "./venv"
        PYTHON = "${VENV}/bin/python"
        PIP = "${VENV}/bin/pip"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    ${PIP} install --upgrade pip
                    ${PIP} install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    ${PIP} install flake8
                    ${VENV}/bin/flake8 app || true
                '''
            }
        }

        stage('Security (SAST & SCA)') {
            steps {
                sh '''
                    ${PIP} install bandit safety
                    ${VENV}/bin/bandit -r app || true
                    ${VENV}/bin/safety check --full-report || true
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    ${PIP} install pytest
                    PYTHONPATH=$PWD ${VENV}/bin/pytest tests
                '''
            }
        }

        stage('Run Flask App') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                sh '''
                    echo "Starting Flask App in background..."
                    export FLASK_APP=app
                    export FLASK_ENV=development
                    ${VENV}/bin/flask run > flask.log 2>&1 &
                    FLASK_PID=$!
                    echo "Flask is running with PID $FLASK_PID"

                    # Optionally test the running app
                    sleep 5
                    curl --silent http://127.0.0.1:5000 || echo "Failed to reach Flask app."

                    # Stop the Flask server after test
                    kill $FLASK_PID
                    echo "Flask server stopped."
                '''
            }
        }
    }
}

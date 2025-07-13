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
                    echo "Running Flask App..."
                    export FLASK_APP=app
                    export FLASK_ENV=development

                    # Run with explicit host binding
                    ${VENV}/bin/flask run --host=0.0.0.0 --port=5000 > flask.log 2>&1 &
                    FLASK_PID=$!

                    # Wait for Flask to boot
                    sleep 5

                    echo "Testing Flask endpoint..."
                    curl -s http://localhost:5000 || echo "Flask app did not respond"

                    kill $FLASK_PID
                    echo "Flask server stopped."
                '''
            }
        }
    }
}

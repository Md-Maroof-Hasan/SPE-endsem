pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Md-Maroof-Hasan/SPE-endsem'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'sonar-scanner'

                    withSonarQubeEnv('sonarqube') {

                        sh """
                        ${scannerHome}/bin/sonar-scanner \
                        -Dsonar.projectKey=secure-notes-api \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://localhost:9000
                        """

                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t auth-service ./auth-service'
            }
        }
        stage('Trivy Scan') {
            steps {
                sh 'trivy image auth-service'
                sh 'trivy image notes-service'
                sh 'trivy image audit-service'
            }
        }
        stage('Deploy Containers') {
            steps {
                sh 'docker compose up -d --build'
            }
        }
    }
}

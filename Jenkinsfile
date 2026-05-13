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
                sh 'docker build -t notes-service ./notes-service'
                sh 'docker build -t audit-service ./audit-service'
            }
        }
        stage('Trivy Scan') {
            steps {
                sh 'trivy image --exit-code 1 --severity CRITICAL auth-service'
                sh 'trivy image --exit-code 1 --severity CRITICAL notes-service'
                sh 'trivy image --exit-code 1 --severity CRITICAL audit-service'
            }
        }
//	stage('Debug Jenkins Path') {
//   	     steps {
//       		 sh 'whoami'
//       		 sh 'pwd'
//       		 sh 'ls -la /'
//       		 sh 'ls -la /var'
//       		 sh 'ls -la /var/jenkins_home'
//       		 sh 'find / -name ".vault_pass.txt" 2>/dev/null'
//       	    }
//	}
        stage('Deploy Containers') {
            steps {
                sh 'ansible-playbook -i ansible/inventory.ini ansible/deploy.yml --vault-password-file /var/lib/jenkins/.vault_pass.txt'
            }
        }
        stage('OWASP ZAP Scan') {
 	   steps {
       		 sh '''
       		 docker run --rm --network host zaproxy/zap-stable \
       		 zap-baseline.py -I -t http://localhost
       		 '''
   	    }
	}
    }
}

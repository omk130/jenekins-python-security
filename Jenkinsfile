pipeline {

    agent any 

    stages{
        stage('Checkout Repo'){
            steps{
                git branch: 'main',
                url: 'https://github.com/omk130/jenekins-python-security.git'
            }
        }


        stage('Install Dependencies'){
            steps{
                 bat 'python -m pip install -r requirements.txt'
            }
        }


        stage('Static Code Analysis'){
            steps{
                bat 'pytlint app.py'
            }
        }


        stage('Dependency Check'){
            steps{
                bat 'safety scan'
            }
        }


        stage('Trivy Scan'){
            steps{
                bat 'trivy fs . > trivy_report.txt'
            }
        }

    }
        post{
            always{
                archiveArtifacts artifacts: 'trivy-report.txt'
            }
        }
}
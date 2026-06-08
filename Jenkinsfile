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
                bat 'python -m pylint app.py'
            }
        }


        stage('Dependency Check'){
            steps{
                bat 'python -m safety scan --ignore'
            }
        }


        stage('Trivy Scan'){
            steps{
                bat 'python -m trivy fs . > trivy_report.txt'
            }
        }

    }
        post{
            always{
                archiveArtifacts artifacts: 'trivy-report.txt'
            }
        }
}
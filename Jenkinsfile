pipeline {

    agent any 

    stages{
        stage('Checkout'){
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
                bat 'python -m safety check'
            }
        }


        stage('Trivy Scan'){
            steps{
                bat "C:\\trivy_0.71.0_windows-64bit\\trivy.exe fs . > trivy_report.txt"
            }
        }

    }
}
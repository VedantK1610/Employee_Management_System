pipeline {

    agent any


    stages {


        stage('Checkout') {

            steps {

                git branch: 'main',
                url: 'https://github.com/VedantK1610/Employee_Management_System.git'

            }
        }




        stage('Build and Run Docker') {

            steps {

                sh 'docker compose down'

                sh 'docker compose up -d'

            }

        }


    }


    post {

        success {

            echo "Deployment Successful"

        }


        failure {

            echo "Deployment Failed"

        }

    }

}
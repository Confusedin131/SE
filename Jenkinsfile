/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.11.5-alpine3.18' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}

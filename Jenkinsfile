pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                echo 'Hello world 3!' 
            }
        }
        stage('Stage 2') {
            steps {
                if(currentBuild.result == null) {
                    echo 'Null build'
                } else {
                    echo 'Not null build'
                }
            }
        }
    }
}
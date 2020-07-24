pipeline {
    agent any
    stages {
        stage('Stage 1') {
            steps {
                echo 'Hello world 3!'
            }
        }
        stage('Stage 2') {
            when {
                expression {
                    currentBuild.result == null
                }
            }
            steps {
                echo 'build is null'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
        stage('Stage 3') {
            when {
                expression {
                    currentBuild.result != null
                }
            }
            steps {
                echo 'build not null'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
    }
}

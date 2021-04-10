pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        echo 'Testing'
        sh 'readlink -f testbot'
        sh 'docker cp d075af177957:./testbot /home/vhserver'
      }
    }

  }
}
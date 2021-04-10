pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        echo 'Testing'
        sh '''ls -a
ls -a ../
 ls ../../
ls /'''
        sh 'docker cp d075af177957:./testbot /home/vhserver'
      }
    }

  }
}
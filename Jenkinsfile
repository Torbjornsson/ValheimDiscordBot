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
        sh 'docker cp -r testbot /home/vhserver'
      }
    }

  }
}
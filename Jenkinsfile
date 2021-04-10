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
      }
    }

  }
}
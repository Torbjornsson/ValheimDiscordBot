pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        echo 'Testing'
        sh 'readlink -f testbot'
        sh 'cp -r testbot /home/vhserver/ValheimDiscordBot'
      }
    }

  }
}
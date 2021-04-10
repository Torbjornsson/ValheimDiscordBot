pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        echo 'Testing'
        sh 'whoami'
        sh 'cp -r testbot /home/vhserver/ValheimDiscordBot'
      }
    }

  }
}
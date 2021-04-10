pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        echo 'Copying Files'
        sh 'cp -r testbot /home/vhserver/python/ValheimDiscordBot'
        sh 'sudo systemctl restart valheimbot.service'
      }
    }

  }
}
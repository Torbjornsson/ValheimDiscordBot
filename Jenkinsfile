pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        echo 'Copying Files'
        sh 'cp -r testbot /home/vhserver/python/ValheimDiscordBot'
        echo 'Restarting Bot'
        sh 'systemctl restart valheimbot.service'
      }
    }

  }
}
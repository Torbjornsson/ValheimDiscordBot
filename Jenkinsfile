pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        echo 'Testing'
        sh 'readlink -f testbot'
        sh 'docker cp d075af177957:/var/jenkins_home/workspace/ValheimDiscordBot_main/testbot /home/vhserver'
      }
    }

  }
}
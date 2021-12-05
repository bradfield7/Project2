pipeline {
    agent any
    stages {
        stage('Run unit tests') {
            steps {
                sh "bash test.sh"
            }
        }
        stage('Build and push images') {
            environment {
                DOCKER_UNAME = credentials('docker_uname')
                DOCKER_PWORD = credentials('docker_pword')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "docker-compose push"
            }
        }
        stage('Deploy') {
            steps {
                sh "scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml swarmmanager:/home/jenkins/docker-compose.yaml"
                sh "scp -i ~/.ssh/ansible_id_rsa nginx.conf swarmmanager:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i config/inventory.yaml config/playbook.yaml"
            }
        }
    }
    
    }
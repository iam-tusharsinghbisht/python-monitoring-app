@Library("Shared") _
pipeline {
    
    agent any
    
    environment {
        CREDENTIALS_ID = 'dockerhub-cred'
    }
    
    stages {
        
        stage("Message"){
            steps{
                script{
                    message()
                }
            }
        }
        
        stage("Code") {
            steps {
                script{
                      echo "Cloining the code from Github repository!"
                      clone("https://github.com/iam-tusharsinghbisht/python-monitoring-app.git", "main")
                      echo "Repository cloned successfully"
                }
            }
        }
        
        stage("Build-Image") {
            steps {
                script{
                    echo "Creating Docker Image"
                    docker_build("monitoring-app", "latest", "shadowlord13")
                }
            }
        }
        
        stage("Push-Image") {
            steps {
                script{
                    echo "Push Docker Image to remote container Registery"
                    docker_push("monitoring-app", "latest", "shadowlord13", env.CREDENTIALS_ID)
                }
            }
        }
        
        
        stage("Deploy") {
            steps {
                script{
                    echo "Deploying the Application"
                    docker_compose()
                }
            }
        }
    }
}
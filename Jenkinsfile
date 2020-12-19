pipeline{
    agent none
    options{
        skipsStageAfterUnstable()
    }
    stages{
        stage('Build'){
            agent{
                docker {
                    image 'python:3-alpine'
                }
            }
            steps{
                sh 'python3 -m py_compile sources/Address_book.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
        stage('Test'){
            agent{
                docker{
                    image 'qnib/pytest'
                }
            }
            steps{
                sh 'py.test --junit-xml test-reports/results.xml sources/application_testing.py'

            }
            post {
                always{
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver'){
            agent any
            environment {
                VOLUME= '$(pwd)/sources:/src'
                IMAGE= 'cdrx/pyinstaller-linux:python3'
            }
            steps{
                dir(path: env.BUILD_ID){
                    unstash(name: 'compiled-results')
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F Address_book.py'"
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/sources/dist/Address_book"
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }


}
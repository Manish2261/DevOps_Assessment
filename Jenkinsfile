  
pipeline{
    agent none
    options{
        skipStagesAfterUnstable()
    }
    stages{
        stage('Pre-Build Email Test') {
            steps{
            mail bcc: '', body: '''Hello Manish,
                This is to inform you that a build is initiated for your project of kpit_pipeline.
                Thanks and Regards,
                Manish G Agrawal''', cc: '', from: '', replyTo: '', subject: 'Alert of Pre-Build of DevOps Pipeline', to: 'mag70452261@gmail.com'
                 }
            }    
           
        stage('Build'){
            agent{
                docker {
                    image 'python:3-alpine'
                }
            }
            steps{
                sh 'python3 -m py_compile sources/Address_book.py sources/Test_Func.py'
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
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F Address_book.py '"
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/sources/dist/Address_book"
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
	    stage('Post-Build Email Test') {
            steps{
            mail bcc: '', body: '''Hello Manish,
                This is to inform you that a build is completed for your project of kpit_pipeline.
                Thanks and Regards,
                Manish G Agrawal''', cc: '', from: '', replyTo: '', subject: 'Alert of Post-Build of DevOps Pipeline', to: 'mag70452261@gmail.com'
            }
            post {
             always { 
                mail to: 'mag70452261@gmail.com',
                subject: "Status of pipeline: ${currentBuild.fullDisplayName}",
                body: "${env.BUILD_URL} has result ${currentBuild.result}"
                }
            }
        }
	}	
}		

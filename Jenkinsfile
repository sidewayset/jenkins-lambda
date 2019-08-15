def bucket = 'set-lamba-fibo'
def functionName = 'Fibonacci'
def region = 'us-west-2'

node('slaves'){
    stage('Checkout'){
        checkout scm
    }

    stage('Test'){
      
    }

    stage('Build'){
        sh 'GOOS=linux go build -o main main.go'
        sh 'python -m py_compile sources/fibonnaci.py'
    }

    stage('Push'){
        sh "aws s3 cp ${commitID()}.zip s3://${bucket}"
    }

    stage('Deploy'){
        sh "aws lambda update-function-code --function-name ${functionName} \
                --s3-bucket ${bucket} \
                --s3-key ${commitID()}.zip \
                --region ${region}"
    }
}

def commitID() {
    sh 'git rev-parse HEAD > .git/commitID'
    def commitID = readFile('.git/commitID').trim()
    sh 'rm .git/commitID'
    commitID
}
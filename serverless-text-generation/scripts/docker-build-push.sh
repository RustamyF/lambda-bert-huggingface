docker build -t bert-textgen-lambda:v1 .
docker tag bert-textgen-lambda:v1 $aws_account_id.dkr.ecr.$aws_region.amazonaws.com/bert-lambda:bert-textgen-lambda
docker push $aws_account_id.dkr.ecr.$aws_region.amazonaws.com/bert-lambda:bert-textgen-lambda


# docker run -p 8080:8080 bert-textgen-lambda:v1

# curl --request POST \
#   --url http://localhost:8080/2015-03-31/functions/function/invocations \
#   --header 'Content-Type: application/json' \
#   --data '{"body":"{\"prompt\":\"My name is Thomas. My main concern with the new govermnet is that it will be slow. I dont want to \", \n\"max_length\":30}"}'

# #!/bin/bash

# curl -X POST https://8lskb7ulb0.execute-api.us-east-1.amazonaws.com/dev/textgen -H "Content-Type: application/json" --data-binary @- <<DATA
# {"prompt": "My name is Thomas. My main concern with the new govermnet is that it will be slow. I dont want to",
# "max_length": 30
# }

# DATA

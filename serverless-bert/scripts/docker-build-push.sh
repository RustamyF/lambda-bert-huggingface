docker build -t bert-lambda:v1 ..
docker tag bert-lambda:v1 $aws_account_id.dkr.ecr.$aws_region.amazonaws.com/bert-lambda:v1
docker push $aws_account_id.dkr.ecr.$aws_region.amazonaws.com/bert-lambda:v1
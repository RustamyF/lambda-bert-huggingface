import json
import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, AutoConfig
import boto3
import os
import uuid
import time

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])


def encode(tokenizer, question, context):
    """encodes the question and context with a given tokenizer
    that is understandable to the model"""
    encoded = tokenizer.encode_plus(question, context)
    return encoded["input_ids"], encoded["attention_mask"]


def decode(tokenizer, token):
    """decodes the tokens to the answer with a given tokenizer
    to return human readable response in a string format"""
    answer_tokens = tokenizer.convert_ids_to_tokens(token, skip_special_tokens=True)
    return tokenizer.convert_tokens_to_string(answer_tokens)


def serverless_pipeline(model_path="./model"):
    """Initializes the model and tokenzier and returns a predict function that ca be used as pipeline"""
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForQuestionAnswering.from_pretrained(model_path)

    def predict(question, context):
        """predicts the answer on an given question and context.
        Uses encode and decode method from above"""
        input_ids, attention_mask = encode(tokenizer, question, context)
        start_scores, end_scores = model(
            torch.tensor([input_ids]), attention_mask=torch.tensor([attention_mask])
        )
        ans_tokens = input_ids[
            torch.argmax(start_scores) : torch.argmax(end_scores) + 1
        ]
        answer = decode(tokenizer, ans_tokens)
        return answer

    return predict


# initializes the pipeline
question_answering_pipeline = serverless_pipeline()


def handler(event, context):
    try:
        # loads the incoming event into a dictonary
        body = json.loads(event["body"])
        # uses the pipeline to predict the answer
        answer = question_answering_pipeline(
            question=body["question"], context=body["context"]
        )
        timestamp = str(time.time())
        item = {
            "primary_key": str(uuid.uuid1()),
            "createdAt": timestamp,
            "context": body["context"],
            "question": body["question"],
            "answer": answer,
        }
        table.put_item(Item=item)
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps({"answer": answer}),
        }
    except Exception as e:
        print(repr(e))
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps({"error": repr(e)}),
        }

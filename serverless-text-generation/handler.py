import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig


def encode(tokenizer, prompt):
    """encodes the question and context with a given tokenizer
    that is understandable to the model"""
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    return input_ids


def decode(tokenizer, token):
    """decodes the tokens to the answer with a given tokenizer
    to return human readable response in a string format"""
    answer_tokens = tokenizer.batch_decode(token, skip_special_tokens=True)
    return answer_tokens[0]


def serverless_pipeline(model_path="./model"):
    """Initializes the model and tokenzier and returns a predict function that ca be used as pipeline"""
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)

    def predict(prompt):
        """predicts the answer on an given question and context.
        Uses encode and decode method from above"""
        input_ids = encode(tokenizer, prompt)
        ans_tokens = model.generate(input_ids, do_sample=False, max_length=60)
        answer = decode(tokenizer, ans_tokens)
        return answer

    return predict


# initializes the pipeline
text_generating_pipeline = serverless_pipeline()


def handler(event, context):
    try:
        # loads the incoming event into a dictonary
        body = json.loads(event["body"])
        # uses the pipeline to predict the answer
        answer = text_generating_pipeline(prompt=body["prompt"])
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

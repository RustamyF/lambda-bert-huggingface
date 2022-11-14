from transformers import AutoTokenizer, AutoModelForCausalLM


def get_model(model):
    """Loads model from Hugginface model hub into
    the ./model directory"""
    try:
        model = AutoModelForCausalLM.from_pretrained(model, use_cdn=True)
        model.save_pretrained("./model")
    except Exception as e:
        raise (e)


def get_tokenizer(tokenizer):
    """Loads tokenizer from Hugginface model hubinto
    the ./model directory"""
    try:
        tokenizer = AutoTokenizer.from_pretrained(tokenizer)
        tokenizer.save_pretrained("./model")
    except Exception as e:
        raise (e)


get_model("distilgpt2")
get_tokenizer("distilgpt2")

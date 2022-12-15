import sys
import os

# sys.path.append("../")

from serverless_bert_qa.get_model import get_model, get_tokenizer
import unittest


class TestDuplicateZeros(unittest.TestCase):
    def test_get_model(self):
        with self.assertRaises(Exception) as context:
            get_model("iuuiiu")
        self.assertTrue("Can't load config for 'iuuiiu'" in str(context.exception))

    def test_get_model_correct(self):
        get_model("mrm8488/mobilebert-uncased-finetuned-squadv2")
        self.assertTrue("config.json" in set(os.listdir("model/")))

    def test_get_tokenizer(self):
        with self.assertRaises(Exception) as context:
            get_tokenizer("iuuiiu")
        self.assertTrue("Can't load config for 'iuuiiu'" in str(context.exception))

    def test_get_tokenizer_correct(self):
        get_tokenizer("mrm8488/mobilebert-uncased-finetuned-squadv2")
        self.assertTrue("tokenizer_config.json" in set(os.listdir("model/")))


if __name__ == "__main__":
    unittest.main()

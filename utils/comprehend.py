import os
import boto3

class Comprehend:

    def __init__(self):
        self.client = boto3.client('comprehend',
        aws_access_key_id=os.environ.get("ACCESS_KEY", ""),
        aws_secret_access_key=os.environ.get("SECRET_KEY", ""),
        region_name=os.environ.get("REGION_NAME", "us-east-1"),
        )

    def detectar_sentimento(self, texto):
        result = self.client.detect_sentiment(Text=texto, LanguageCode='pt')
        return result

    def detectar_palavra_chave(self, texto):
        result = self.client.detect_key_phrases(Text=texto, LanguageCode='pt')
        return result

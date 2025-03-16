from __future__ import print_function
import time
import boto3

vocabulary_bucket = 'tnobe-transcribe'
vocabulary_key = 'custom-vocabulary/my-vocabulary.txt'
vocabulary_uri = f's3://{vocabulary_bucket}/{vocabulary_key}'

transcribe = boto3.client('transcribe')
vocab_name = "my-first-vocabulary"

response = transcribe.create_vocabulary(
    LanguageCode = 'ja-JP',
    VocabularyName = vocab_name,
    VocabularyFileUri = vocabulary_uri
)

while True:
    status = transcribe.get_vocabulary(VocabularyName = vocab_name)
    if status['VocabularyState'] in ['READY', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
print(status)
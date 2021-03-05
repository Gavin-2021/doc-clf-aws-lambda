import json
import pandas as pd
from imblearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import RandomOverSampler
from sklearn.ensemble import RandomForestClassifier
import joblib
import boto3
from io import BytesIO


def get_model():
    bucket = boto3.resource("s3").Bucket("doc-clf-ml")
    with BytesIO() as modelfo:
        bucket.download_fileobj(Key="model/doc_clf_light_model.pkl", Fileobj = modelfo)
        model = joblib.load(modelfo)
    return model

def predict(event, context):
    
    body = {
        "message": "Document Clasification"
    }

    params = event['queryStringParameters']

    hashCode = pd.Series(params['hashCode'])

    model = get_model()

    predicted = model.predict(hashCode).tolist()
    body['predictedDoc'] = predicted

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers":{
            "Access-Control-Allow-Origin": "*"
        }
    }

    return response

def do_main():
    
    event = {
        'queryStringParameters': {
            'hashCode': "f1e85a5fea9 3114e0d45526 8159faa9d80d a8fa53f71d53 75f02c08e202 365a9390d225 e943e5e5b779 e6c582b41a2f dcbfe39d6d81 586242498a88 e6c582b41a2f 277835dc10c2 bc9828c704f5 fe64d3cdfe5b 31e8970bd827 1b398b5b9d07 6ca2dd348663 d38820625542 089e3092ac55 fc442cf33ad9 9e0c01b8b857 20d53168dbb6 236eeaf59a18 d5f4611022c1 2b2acdf4a3ed f52871480463 0d5c6a460006 360e8b28421c 118931ca018b fe3fe35491b4 9f11111004ec 3fc879c6be39 c337a85b8ef9 17bd1f49c9a0 efa618f37f68 1015893e384a 586242498a88 586242498a88 7b4f94127c27 fe64d3cdfe5b 1b76aac2823a 04503bc22789 dd75c377a2f9 9e60e37e5680 6bf9c0cb01b4 40eae65031b9 0562c756a2f2 fb279192f4cf e35ff0f5e23c dc1e926e1c1f ce1f034abb5d d23310899072 6bf9c0cb01b4 d8afd84c6fa9 c337a85b8ef9 b9699ce57810 e08ed9a28ce1 730b6a62640b 957b5cf4e65e 1015893e384a 5e99d31d8fa4 7d7400d32c11 93790ade6682 61b7e0f00ffe f706a5d38c07 4357c81e10c1 5c02c2aaa67b 5e99d31d8fa4 b208ae1e8232 036087ac04f9 b136f6349cf3 586242498a88 d0a6ba7c50bf 6bb0aa622b46 d85aeb8537e1 fe64d3cdfe5b 9cdf4a63deb0 b274cd8dd187 774445039259 a31962fbd5f3 75440bb763a2 be95012ebf2b 6ef2ade170d9 a8fa53f71d53 75f02c08e202 0b5b01c84bb1 c337a85b8ef9 d8afd84c6fa9 580a08f5c8b9 089e3092ac55 1c9cbc210946 20d53168dbb6 dd75c377a2f9 93f74477ec1d cf2205dbb077 6ce6cc5a3203 a9ee836e8303 ad5812612e12 c33578d25a0d 958ca775aa7a 8f75273e5510 fd43f99e9b26 6b304aabdcee 6ca2dd348663 d38820625542 9e0c01b8b857 236eeaf59a18 43d186e2a89e 6ce6cc5a3203 6ce6cc5a3203 6a01047db3ab abe7d2dd7c9b 93293c8fc69e 10e45001c2f2 064f6365a9cd 089e3092ac55 1c9cbc210946 2b2acdf4a3ed 5fa5ede74901 a8fc3bc65e35 b9449cdbfd65 43c334389208 938e3cea29d2 26f768da5068 6af770640118 e43c4b6f2c61 4d94d10e3a36 a9bb134e7fcd c33578d25a0d 7dd73db6309f 958ca775aa7a 8f75273e5510 fd43f99e9b26 7fece2c25d8a 17850ce2d9b5 c66a823799c1 5be138559904 ea51fa83c91c cbfb3eb99bea"
        }
    }

    response = predict(event, None)
    body = json.loads(response['body'])
    print('Label: ', body['predictedDoc'])

    with open('event.json', 'w') as event_file:
        event_file.write(json.dumps(event))

if __name__ == "__main__":
    do_main()

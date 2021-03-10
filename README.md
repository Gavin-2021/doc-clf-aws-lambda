# doc-clf-aws-lambda
This repo contains the full code and toy data to train a document classifier and templates needed to create a serverless web service using AWS lambda functions.

Random Forest is used as the classifier. The original model has 0.8169 in accuracy in testing data and 0.8188 in training. But it cannot be on AWS since the model is a big large and it would time out when performing prediction on AWS. A ligher version is being used on cloud with 0.7875 in accuracy. Confusion matrices can be found in jupyter notebook script. 

## doc_clf_tryout1.ipynb
Model training script using jupyter notebook

## handler.py
Model pipeline with lambda functions.

## serverless.yml
Configurition file for AWS serverless deployment

## shuffled-full-set-hashed.csv.zip
Original data set

## doc_clf_best_estimator.pkl
The ligher version of model file which is being used on AWS

Web URL: https://4iia82hd7a.execute-api.us-west-1.amazonaws.com/dev

Example:

https://4iia82hd7a.execute-api.us-west-1.amazonaws.com/dev/get-doc-clf?hashCode="f1e85a5fea9 3114e0d45526 8159faa9d80d a8fa53f71d53 75f02c08e202 365a9390d225 e943e5e5b779 e6c582b41a2f dcbfe39d6d81 586242498a88 e6c582b41a2f 277835dc10c2 bc9828c704f5 fe64d3cdfe5b 31e8970bd827 1b398b5b9d07 6ca2dd348663 d38820625542 089e3092ac55 fc442cf33ad9 9e0c01b8b857 20d53168dbb6 236eeaf59a18 d5f4611022c1 2b2acdf4a3ed f52871480463 0d5c6a460006 360e8b28421c 118931ca018b fe3fe35491b4 9f11111004ec 3fc879c6be39 c337a85b8ef9 17bd1f49c9a0 efa618f37f68 1015893e384a 586242498a88 586242498a88 7b4f94127c27 fe64d3cdfe5b 1b76aac2823a 04503bc22789 dd75c377a2f9 9e60e37e5680 6bf9c0cb01b4 40eae65031b9 0562c756a2f2 fb279192f4cf e35ff0f5e23c dc1e926e1c1f ce1f034abb5d d23310899072 6bf9c0cb01b4 d8afd84c6fa9 c337a85b8ef9 b9699ce57810 e08ed9a28ce1 730b6a62640b 957b5cf4e65e 1015893e384a 5e99d31d8fa4 7d7400d32c11 93790ade6682 61b7e0f00ffe f706a5d38c07 4357c81e10c1 5c02c2aaa67b 5e99d31d8fa4 b208ae1e8232 036087ac04f9 b136f6349cf3 586242498a88 d0a6ba7c50bf 6bb0aa622b46 d85aeb8537e1 fe64d3cdfe5b 9cdf4a63deb0 b274cd8dd187 774445039259 a31962fbd5f3 75440bb763a2 be95012ebf2b 6ef2ade170d9 a8fa53f71d53 75f02c08e202 0b5b01c84bb1 c337a85b8ef9 d8afd84c6fa9 580a08f5c8b9 089e3092ac55 1c9cbc210946 20d53168dbb6 dd75c377a2f9 93f74477ec1d cf2205dbb077 6ce6cc5a3203 a9ee836e8303 ad5812612e12 c33578d25a0d 958ca775aa7a 8f75273e5510 fd43f99e9b26 6b304aabdcee 6ca2dd348663 d38820625542 9e0c01b8b857 236eeaf59a18 43d186e2a89e 6ce6cc5a3203 6ce6cc5a3203 6a01047db3ab abe7d2dd7c9b 93293c8fc69e 10e45001c2f2 064f6365a9cd 089e3092ac55 1c9cbc210946 2b2acdf4a3ed 5fa5ede74901 a8fc3bc65e35 b9449cdbfd65 43c334389208 938e3cea29d2 26f768da5068 6af770640118 e43c4b6f2c61 4d94d10e3a36 a9bb134e7fcd c33578d25a0d 7dd73db6309f 958ca775aa7a 8f75273e5510 fd43f99e9b26 7fece2c25d8a 17850ce2d9b5 c66a823799c1 5be138559904 ea51fa83c91c cbfb3eb99bea"

output:
{"message": "Document Classification", "predictedDoc": ["CANCELLATION NOTICE"]}



# Deployment steps:

1. Create conda virsual env and install required packages
2. Create serverless template files
```sh
sls create --template aws-python3 --name doc-clf
```
3. Build model pipeline - handler.py
4. Config serverless.yml
5. Invoke lambda function locally and test the function using event.json file
```sh
sls invoke local --function doc-clf --path event.json
```
6. Create s3 bucket and upload model file
```sh
aws s3api create-bucket --acl private --bucket doc-clf-ml --create-bucket-configuration LocationConstraint=us-west-1
aws s3 cp doc_clf_best_estimator.pkl s3://doc-clf-ml/model/doc_clf_light_model.pkl
```
8. Install plugin
```sh
sls plugin install -n serverless-python-requirements
```
9. Deployment
```
sudo sls deploy
```
10. Invoke handler globally and test it with event.json file
```sh
sls invoke --function doc-clf --path event.json
```

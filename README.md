# doc-clf-aws-lambda
This repo contains the full code and toy data to train a document classifier and templates needed to create a serverless web service using AWS lambda functions.

Random Forest is used as the classifier. The original model has 0.818770071309834 in accuracy in testing data and 0.818770071309834 in training. But it cannot be on AWS since the model is a big large and it would time out when performing prediction on AWS. A ligher version is being used on cloud with 0.7874839124839125 in accuracy. Confusion matrices can be found in jupyter notebook script. 

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

Web url: https://4iia82hd7a.execute-api.us-west-1.amazonaws.com/dev


# Delopyment steps:

1. create conda virsual env and install required packages
2. create serverless template files
'''sh
sls create --template aws-python3 --name doc-clf
'''
3. build model pipeline - handler.py
4. config serverless.yml
5. invoke lambda function locally and test the function using event.json file
```sh
sls invoke local --function doc-clf --path event.json
```
6. create s3 bucket and upload model file
```sh
aws s3api create-bucket --acl private --bucket doc-clf-ml --create-bucket-configuration LocationConstraint=us-west-1
aws s3 cp doc_clf_best_estimator.pkl s3://doc-clf-ml/model/doc_clf_light_model.pkl
```
8. install plugin
```sh
sls plugin install -n serverless-python-requirements
```
9. deployment
```
sudo sls deploy
```
10. invoke handler globally and test it with event.json file
```sh
sls invoke --function doc-clf --path event.json
```

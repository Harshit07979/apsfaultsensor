import pymongo
import pandas as pd
import json
#providing local host url to coonect to mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/")

#create database name and collection name
DATABASE_NAME= "sensoredetector"
COLLECTION_NAME = "sensoredata"
DATA_FILE_PATH= "E:/sensordetection/aps_failure_training_set1.csv"

if __name__== "__main__":
    #read data from csv file and store it in database
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns in dataset {df.shape} ")
    #convert this datafram into json so that we can dump it into mongodb
    df.reset_index(drop=True, inplace=True)
#loading json in list from json.load and getting its values
    json_record= list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    #insert converted json record to mongo db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)





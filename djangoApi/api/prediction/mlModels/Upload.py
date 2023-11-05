import pymongo
import gridfs
import os

mongo_uri = "mongodb://localhost:27017"
db_name = "MLModels"

client = pymongo.MongoClient(mongo_uri)
db = client[db_name]
fs = gridfs.GridFS(db)


dir = os.path.dirname(os.path.abspath(__file__))
modelPath = dir + "\consumer_complaint_model.pkl"
VectorizerPath = dir + "\\fittedVectorizer.pkl"


with open(modelPath, "rb") as model_file:
    data = model_file.read()

model_file_id = fs.put(data, filename="consumer_complaint_model.pkl")
print("Model file uploaded with ID:", model_file_id)


with open(VectorizerPath, "rb") as Vectorizer_file:
    data = Vectorizer_file.read()

vectorizor_file_id = fs.put(data, filename="fittedVectorizer.pkl")
print("Vectorizer file uploaded with ID:", vectorizor_file_id)

import pymongo
import gridfs
import pickle

def predictLoanType(predictionData):

    mongo_uri = "mongodb://localhost:27017"
    db_name = "MLModels"

    client = pymongo.MongoClient(mongo_uri)
    db = client[db_name]
    fs = gridfs.GridFS(db)

    # Retrieve Model Data
    model_file = fs.find_one({"filename": "consumer_complaint_model.pkl"})
    serialized_model_data = model_file.read()
    loaded_model = pickle.loads(serialized_model_data)

    # Retrieve fitted Vectorizer Data
    vectorizer_file = fs.find_one({"filename": "fittedVectorizer.pkl"})
    serialized_vectorizer_data = vectorizer_file.read()
    fitted_Vectorizer = pickle.loads(serialized_vectorizer_data)

    pred = loaded_model.predict(fitted_Vectorizer.transform([predictionData]))
    return pred

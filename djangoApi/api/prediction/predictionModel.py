import pickle
import os

def predictLoanType(predictionData):

    dir = os.path.dirname(os.path.abspath(__file__))
    modelPath = dir + "\mlModels\consumer_complaint_model"
    VectorizerPath = dir + "\mlModels\\fittedVectorizer"

    
    loaded_model = pickle.load(open(modelPath, 'rb'))
    fitted_Vectorizer = pickle.load(open(VectorizerPath, 'rb'))
    pred = loaded_model.predict(fitted_Vectorizer.transform([predictionData]))
    return pred

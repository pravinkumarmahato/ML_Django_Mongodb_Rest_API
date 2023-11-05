from rest_framework.response import Response
from rest_framework.decorators import api_view
from .prediction.predictionModel import predictLoanType

@api_view(['POST'])
def postData(request):
    predictionData = request.data["name"]
    # print(predictionData)
    pred = predictLoanType(predictionData)
    # pred = 'abc'
    predictedValue = { 'prediction String': predictionData, 'Predicted Value': pred }
    return Response(predictedValue)


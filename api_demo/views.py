from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging # to set loggers

logger = logging.getLogger('django')

# Create your views here.
@api_view(['GET']) # we use api_view() decorator to convert our view method to http method
def load_user(request):
    user = User.objects.all()
    # we need to serialize the query set to json format, so here we use UserSerializer class defined in serializers.py
    serialized_data = UserSerializer(user,many = True)
    # if the query set contains multiple data, we must use many = True argument
    return Response(serialized_data.data)

@api_view(['POST'])
def add_user(request):
    user_data = request.data
    serialized_data = UserSerializer(data = user_data) # here we convert json data to python datatype
    
    if serialized_data.is_valid():
        serialized_data.save()
        satatus_code = 201 # use 201 when insert a data
    else:
        satatus_code = 500
    return Response({'status': satatus_code})

@api_view(['PUT'])
def update_user(request,user_id): # here user_id will be sent through url from front end
    user = User.objects.get(id = user_id) # fetching the user object with corresponding user object with data sent from frontend (request.data)
    serialized_data = UserSerializer(user, data = request.data)

    if serialized_data.is_valid():
        serialized_data.save()
        status_code = 200

    else:
        status_code = 500
    return Response({'status':status_code})

@api_view(['DELETE'])
def delete_user(request,user_id):
    user = User.objects.get(id = user_id)

    user.delete()
    status_code = 200
    return Response({'status':status_code})

@api_view(['GET'])
def index(request):
    message = 'Congratulations, you have created an API'
    return Response(message)

@api_view(['GET'])
def return_float(request):
    logger.info('setting logger') # calling logger here
    message = 10.0
    return Response(message)
    
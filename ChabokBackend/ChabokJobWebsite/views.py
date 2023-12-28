from serializers import *
from models import User
from rest_framework.response import Response
from rest_framework import status



def login(request):
    serialized_data = loginSerializer(data=request.data)
    if serialized_data.is_valid(raise_exception=True):
        try:
            user = User.get_user_by_email(email=serialized_data.validated_data['email'])
            if user.password != serialized_data.validated_data['password']:
                return Response(data={'message': 'wrong password'}, status=status.HTTP_400_BAD_REQUEST)
            return Response(data={'message': 'ok'}, status=status.HTTP_200_OK)
        except:
            return Response(data={'message': 'email does not exist'}, status=status.HTTP_400_BAD_REQUEST)
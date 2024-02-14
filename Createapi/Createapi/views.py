from Createapi.serialization import SerializationClass
from Createapi.models import Login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
  # Make sure to import your serializer
# views.py

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Login  # Import your Login model
# from .serializers import LoginSerializer  # Import your LoginSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class SecureEndpoint(APIView):
    def get(self, request):
        # Retrieve all users
        users = User.objects.all()
        
        # Serialize user data
        serialized_users = [{'id': user.id, 'username': user.username} for user in users]
        
        return Response(serialized_users)


    def post(self, request):
        # Your view logic for a POST request
        return Response({"message": "You accessed the secured endpoint with a valid JWT token."})








class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def showemp(request):
    if request.method == 'GET':
        results = Login.objects.all()
        serialize = SerializationClass(results, many=True)
        return Response(serialize.data)

@api_view(['POST'])
def validate(request):
    if request.method == 'POST':
        try:
            username = request.data.get('fname', '')
            password = request.data.get('password', '')

            user = Login.objects.get(name=username)

            # Assuming you are storing passwords as plain text (which is not recommended)
            if user.passs == password:
                message = 'User authenticated successfully'
                return JsonResponse({'message': message}, status=200)
            else:
                message = 'Incorrect password'
                return JsonResponse({'message': message}, status=401)

        except Login.DoesNotExist:
            message = 'User does not exist'
            return JsonResponse({'message': message}, status=404)
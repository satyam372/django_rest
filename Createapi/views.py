from Createapi.serialization import SerializationClass, RaiseissueSerializer,Raiseissue_2Serializer,CombinedComplaintsSerializer
from Createapi.models import Login, Raisecomplaint, Raisecomplaint_2
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .models import Login  
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import generics
from rest_framework import serializers



#  below is the class to retrive the complaints
class CombinedComplaintsView(APIView):
    def get(self, request, emp_id, *args, **kwargs):
        # Get complaints from Raisecomplaint model
        raisecomplaints = Raisecomplaint.objects.filter(emp_id=emp_id)
        raisecomplaints_serializer = CombinedComplaintsSerializer(raisecomplaints, many=True).data

        # Get complaints from Raisecomplaint_2 model
        raisecomplaint_2s = Raisecomplaint_2.objects.filter(emp_id=emp_id)
        raisecomplaint_2s_serializer = CombinedComplaintsSerializer(raisecomplaint_2s, many=True).data

        # Combine the data from both models
        combined_data = raisecomplaints_serializer + raisecomplaint_2s_serializer

        return Response(combined_data)

class Registercomplaint_2(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request, *args, **kwargs):
        posts_2 = Raisecomplaint_2.objects.all()
        Serializer = Raiseissue_2Serializer(posts_2, many=True)
        return Response(Serializer.data)

    def post(self, request, *args, **kwargs):
        regester_serializer=Raiseissue_2Serializer(data=request.data)
        if regester_serializer.is_valid():
            regester_serializer.save()
            return Response(regester_serializer.data,status=status.HTTP_201_CREATED)
        else:
            print('error',regester_serializer.errors)
            return Response(regester_serializer.data,status=status.HTTP_400_BAD_REQUEST)

        


    
class Registercomplaint(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser) 

    def get(self, request, *args, **kwargs):
        posts = Raisecomplaint.objects.all()
        serializer = RaiseissueSerializer(posts, many=True)  # Corrected line
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        register_serializer = RaiseissueSerializer(data=request.data)
        if register_serializer.is_valid():
            register_serializer.save()
            return Response(register_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', register_serializer.errors)
            return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

            
            if user.passs == password:
                message = 'User authenticated successfully'
                return JsonResponse({'message': message}, status=200)
            else:
                message = 'Incorrect password'
                return JsonResponse({'message': message}, status=401)

        except Login.DoesNotExist:
            message = 'User does not exist'
            return JsonResponse({'message': message}, status=404)
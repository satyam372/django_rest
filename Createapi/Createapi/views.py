from Createapi.serialization import SerializationClass, RaiseissueSerializer,Raiseissue_2Serializer
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



#  below is the class to retrive the complaints
class EmployeeComplaintDetailsView(generics.RetrieveAPIView):
    def get(self, request, emp_id, *args, **kwargs):
        # Fetch details from Raisecomplaint model
        raisecomplaint = Raisecomplaint.objects.filter(emp_id=emp_id).first()

        if raisecomplaint is None:
            return Response({"message": "Employee complaint not found"}, status=404)

        # Fetch details from Raisecomplaint_2 model
        raisecomplaint_2 = Raisecomplaint_2.objects.filter(complaint=raisecomplaint)

        # Serialize data from both models
        serializer_raisecomplaint = RaiseissueSerializer(raisecomplaint)
        serializer_raisecomplaint_2 = Raiseissue_2Serializer(raisecomplaint_2, many=True)

        # Combine the data into a single response
        response_data = {
            "raisecomplaint": serializer_raisecomplaint.data,
            "raisecomplaint_2": serializer_raisecomplaint_2.data
        }

        return Response(response_data)













class Registercomplaint_2(APIView):  # class to store complaint into table Raisecomplaint_2
    parser_classes=(MultiPartParser,FormParser,JSONParser) # to parse the json response 

    def get(self,request,*args,**kwargs):  # get request to view the response
        posts_2=Raisecomplaint_2.objects.all()  # to select all objects from the table raisecomplaint_2
        Serializer=Raiseissue_2Serializer(posts_2,many=True) # calling serializer class from serilization.py class
        return Response(Serializer.data) # returning the complaint from the database in json format using serialization


    def post(self,request,*args,**kwargs):  # post request to push the complaint details into table
        register_serilize_2=Raiseissue_2Serializer(data=request.data) # collecting the data
        if register_serilize_2.is_valid():
            register_serilize_2.save() # saving the data into the table Raiseissue_2 table using the serilizer (raiseissue_2serializer)
            return Response(register_serilize_2.data,status.HTTP_201_CREATED)
        else:
            print('error', register_serilize_2.errors)
            return Response(register_serilize_2.errors, status=status.HTTP_400_BAD_REQUEST)

    

    
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
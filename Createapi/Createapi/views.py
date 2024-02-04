from Createapi.serialization import SerializationClass
from Createapi.models import Login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@api_view(['GET'])
def showemp(request):
    if request.method=='GET':
        results=Login.objects.all()
        serialize=SerializationClass(results,many=True)
        return Response(serialize.data)
    
@api_view(['POST'])
def validate(request):

    try:

        user_aaa = User.objects.get(username='aaa')
        print(f"User 'aaa' exists: {user_aaa}")
    except User.DoesNotExist:
       
       print("User 'aaa' does not exist.")

# Query user by username 'ggg'
    try:
        user_ggg = User.objects.get(username='ggg')
        print(f"User 'ggg' exists: {user_ggg}")
    except User.DoesNotExist:
      print("User 'ggg' does not exist.")
    # if request.method == 'POST':
    #     name = request.data.get('name')
    #     passs = request.data.get('passs')

    #     user = authenticate(request, name=name, passs=passs)

    #     if user is not None:
    #         token, created = Token.objects.get_or_create(user=user)
    #         return Response({'success'})
    #     else:
    #         return Response({'error': 'invalid credentials'}, status=401)


# views.py

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate

@api_view(['POST'])
def patient_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None and user.groups.filter(name='Patients').exists():
        refresh = RefreshToken.for_user(user)
        return Response({'token': str(refresh.access_token)})
    return Response({'error': 'Invalid credentials'}, status=400)

@api_view(['POST'])
def doctor_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None and user.groups.filter(name='Doctors').exists():
        refresh = RefreshToken.for_user(user)
        return Response({'token': str(refresh.access_token)})
    return Response({'error': 'Invalid credentials'}, status=400)

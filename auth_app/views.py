from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from auth_app.serializers import UserProfileSerializer

"""
Function based view for the register endpoint.
Since the username is required and a user only set's an email,
the username will be the email too.
Will return the email as response upon success or an error upon failure.
"""
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    data = request.data
    data['username'] = data['email']
    serializer = UserProfileSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        response = {'email': serializer.data['email']}
        return Response(response, status=201)
    response = {'detail': 'Please check your entries and try again.'}
    return Response(response, status=400)

"""
Function based view for the login endpoint.
"""
@api_view(['GET'])
@permission_classes([AllowAny])
def login_view(request):
    #TODO:
    pass
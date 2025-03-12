from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from auth_app.email_confirmation.email_confirmation import send_confirmation_email
from auth_app.models import UserProfile
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
    data['username'] = data['email'].split('@')[0]
    password = data['password']
    serializer = UserProfileSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(password)
        user.save()
        send_confirmation_email(user)
        response = {'email': serializer.data['email']}
        return Response(response, status=201)
    response = {'detail': 'Please check your entries and try again.'}
    return Response(response, status=400)

"""
Handles the click on the activation link from the confirmation email after register.
"""
@api_view(['GET'])
@permission_classes([AllowAny])
def confirm_view(request, token):
    token_obj = get_object_or_404(Token, key=token)
    user = token_obj.user
    user.is_email_confirmed = True
    user.save()
    token_obj.delete()
    new_token = Token.objects.create(user=user)
    return HttpResponseRedirect('http://localhost:4200/login')


class LoginView(ObtainAuthToken):
   permission_classes = [AllowAny]

   def post(self, request):
       serializer = self.serializer_class(data=request.data)
       data = {}
       if serializer.is_valid():
            user = serializer.validated_data['user']
            if(user.is_email_confirmed == True):
                token, created = Token.objects.get_or_create(user=user)
                data = {'token': token.key}
            else:
                data = {'details': 'Please check your email for the account activation link first.'}
       else:
           data = {'details': 'Unable to login with the provided credentials.'}
           return Response(data, status=400)

       return Response(data)
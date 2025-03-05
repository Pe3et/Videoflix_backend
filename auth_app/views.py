from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

"""
Function based view for the register endpoint.
"""
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    #TODO:
    pass


"""
Function based view for the login endpoint.
"""
@api_view(['GET'])
@permission_classes([AllowAny])
def login_view(request):
    #TODO:
    pass
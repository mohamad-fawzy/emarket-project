from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed

def generate_token(username: str, password: str):
    user = authenticate(username=username, password=password)
    if not user:
        raise AuthenticationFailed("اسم المستخدم أو كلمة المرور غير صحيحة")

    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
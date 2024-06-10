from keycloak import KeycloakOpenID,exceptions
keycloak_openid = KeycloakOpenID(
    server_url="http://localhost:8080/auth/",
    realm_name="Lead",
    client_id="account",
    verify=True,
)
from functools import wraps
from django.http import JsonResponse
class decorator:
 def requires_token(func):
    @wraps(func)
    def wrapper(self,request, *args, **kwargs):
        access_token = request.headers.get('Authorization')
        print(access_token)
        if not access_token:
            return JsonResponse({'error': 'Authorization header is missing'}, status=401)

        access_token = access_token[7:]
        try:

            userinfo = keycloak_openid.userinfo(access_token)
            return func(self,request, *args, **kwargs)

        except exceptions.KeycloakError as e:
            return JsonResponse({'error': str(e)}, status=401)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return wrapper
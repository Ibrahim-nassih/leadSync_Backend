from keycloak import KeycloakAdmin
import requests.exceptions


class Keycloak:
    kc_admin = KeycloakAdmin(
    server_url="http://localhost:8080/auth/",
    realm_name='Lead',
    client_id="DjangoPromoteApp1",
    client_secret_key="FEJ3lwqcQ0mQwCOquvray2egS0lqaqHN",
    verify=True
   )
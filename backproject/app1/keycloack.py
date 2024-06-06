from keycloak import KeycloakAdmin
import requests.exceptions


class Keycloak:
    kc_admin = KeycloakAdmin(
    server_url="https://authdev.clinops.app/auth/",
    realm_name='Lead',
    client_id="DjangoPromoteApp1",
    client_secret_key="c99ede1a-08d2-4189-894e-bbfa319c9614",
    verify=True
   )
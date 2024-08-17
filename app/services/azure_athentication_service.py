import os
import time
from msal import PublicClientApplication

# Configurações para a aplicação
client_id = os.environ['CLIENT_ID']
tenant_id = os.environ['TENENT_ID']
authority = f'https://login.microsoftonline.com/{tenant_id}'
scopes = os.environ['SCOPES']
refresh_token = None
access_token = None
id_token = None
token_expiry = None

# Instância da PublicClientApplication
app = PublicClientApplication(client_id, authority=authority)

def authenticate():
    global access_token, refresh_token, id_token, token_expiry

    # Fluxo de autenticação - dispositivo
    flow = app.initiate_device_flow(scopes=scopes)
    if 'user_code' not in flow:
        raise ValueError("Failed to create device flow. Check your client ID and tenant ID.")

    print(f"Go to {flow['verification_uri']} and enter the code {flow['user_code']} to authenticate.")

    result = app.acquire_token_by_device_flow(flow)
    if 'access_token' in result:
        access_token = result['access_token']
        refresh_token = result.get('refresh_token', None)
        id_token = result.get('id_token', None)
        token_expiry = result['expires_in'] + time.time()
    else:
        raise ValueError(f"Authentication failed: {result.get('error_description')}")

def renew_token():
    global access_token, refresh_token, token_expiry

    result = app.acquire_token_by_refresh_token(refresh_token, scopes=scopes)
    if 'access_token' in result:
        access_token = result['access_token']
        token_expiry = result['expires_in'] + time.time()
    else:
        authenticate()

def ensure_authenticated(func):
    def wrapper(*args, **kwargs):
        global access_token, token_expiry

        # Verifica se o usuário está autenticado ou se o token expirou
        if not access_token or time.time() > token_expiry:
            if refresh_token:
                renew_token()
            else:
                authenticate()

        # Executa a função original
        return func(*args, **kwargs)

    return wrapper
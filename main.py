import os
from dotenv import load_dotenv
from msal import PublicClientApplication

load_dotenv()

client_id = os.environ['CLIENT_ID']
tenant_id = os.environ['TENENT_ID']
scopes = ['https://graph.microsoft.com/.default']


app = PublicClientApplication(
  client_id=client_id,
  authority=f"https://login.microsoftonline.com/{tenant_id}"
)

acquire_tokens_result = app.acquire_token_interactive(scopes=scopes)

if 'error' not in acquire_tokens_result:
    print(f"Id token: {acquire_tokens_result['id_token']}\r\n")
    print(f"Access token: {acquire_tokens_result['access_token']}\r\n")
    print(f"Refresh token: {acquire_tokens_result['refresh_token']}\r\n")
else:
    print(f"Error: {acquire_tokens_result['error']}\r\n")
    print(f"Description: {acquire_tokens_result['error_description']}\r\n")

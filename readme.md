# Spike Azure AD Login with Python CLI

## Descrição

Este projeto é uma spike de exploração para implementar a autenticação de usuários no Azure AD utilizando uma CLI escrita em Python. O objetivo é aprender a autenticar usuários de maneira interativa a partir de uma linha de comando (CLI) usando o SDK MSAL (Microsoft Authentication Library) para Python.

## Pré-requisitos

Antes de executar o projeto, certifique-se de atender aos seguintes pré-requisitos:

-   **Registrar um aplicativo no Azure AD**: É necessário registrar um aplicativo no Azure AD para obter os valores de `CLIENT_ID` e `TENANT_ID`. Siga [este link](https://learn.microsoft.com/azure/active-directory/develop/quickstart-register-app) para o guia de registro.
-   **Python 3.11**: Certifique-se de ter o Python 3.11 instalado.
-   **Arquivo .env**: Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:
    -   `CLIENT_ID`: O ID do cliente (Client ID) do aplicativo registrado no Azure AD.
    -   `TENANT_ID`: O ID do inquilino (Tenant ID) do Azure AD.

## Instalação

Para instalar as dependências do projeto, execute o comando abaixo:

bash

Copiar código

`pip install -r requirements.txt` 

## Execução

Para rodar o projeto e iniciar a autenticação no Azure AD, execute o seguinte comando:

bash

Copiar código

`python main.py` 

## Funcionamento

O script `main.py` realiza a autenticação interativa dos usuários no Azure AD, utilizando o SDK MSAL. Ao ser executado, o script faz o seguinte:

1.  Carrega as variáveis de ambiente do arquivo `.env`.
2.  Configura o cliente de autenticação com base no `client_id` e `tenant_id`.
3.  Solicita que o usuário faça login através de uma interface interativa.
4.  Exibe os tokens de ID, acesso e atualização obtidos após a autenticação.

Caso ocorra algum erro durante a autenticação, o script exibirá a descrição do erro.

## Demonstração
![image](https://github.com/tuyoshivinicius/spike-azure-ad-login-with-python-cli/blob/main/images/print1.jpg?raw=true)

![image](https://github.com/tuyoshivinicius/spike-azure-ad-login-with-python-cli/blob/main/images/print2.jpg?raw=true)

![image](https://github.com/tuyoshivinicius/spike-azure-ad-login-with-python-cli/blob/main/images/print3.jpg?raw=true)

![image](https://github.com/tuyoshivinicius/spike-azure-ad-login-with-python-cli/blob/main/images/print4.jpg?raw=true)

## Referências

-   [Documentação do MSAL para Python](https://pypi.org/project/msal/)
-   [Como registrar um aplicativo no Azure AD](https://learn.microsoft.com/azure/active-directory/develop/quickstart-register-app)




# Teste de Habilidades IVIJUR

Este repositório tem como objetivo reunir as respostas para os testes de habilidades propostos pela IviJur.

## Teste 03): Integração com APIs Externas

Para realizar a integração com APIs externas, especialmente quando é necessária autenticação por token, utilizaria este procedimento:

1. **Obtenção do Token de Acesso:**
   - Primeiramente, acessaria o site ou API correspondente para gerar um token de acesso, conforme as orientações fornecidas pela documentação da API.
   - Após gerar o token, o armazenaria em um local seguro, como um arquivo `.env`, que geralmente não é versionado no GitHub, garantindo sua segurança.
   
2. **Utilização do Token no Código Principal:**
   - No código principal, utilizaria a variável que foi definida no arquivo `.env` para acessar o token de forma segura.
   
3. **Inclusão do Token nas Requisições:**
   - Ao realizar uma requisição à API, é provável que o corpo da solicitação exija o token de autenticação. Nesse caso, incluiria o token no corpo da requisição, conforme especificado pela API.

Fontes de Referência:
- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [Tutorial YouTube sobre Integração de APIs](https://www.youtube.com/watch?v=bKCORrHbutQ)

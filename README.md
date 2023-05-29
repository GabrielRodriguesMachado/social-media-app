# Django Social Media App

Django Social Media App é um projeto de exemplo que demonstra o desenvolvimento de uma aplicação simples de mídia social usando o framework Django.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python 3
- pip
- Outras dependências listadas no arquivo `requirements.txt`

## Instalação

1. Clone o repositório ou faça o download do código-fonte.

```bash
git clone git@github.com:GabrielRodriguesMachado/social-media-app.git
```

2. Navegue até o diretório do projeto.
```bash
cd social-media-app
```

3. Crie e ative um ambiente virtual (opcional, mas recomendado).
```bash
python -m venv env # caso o comando não funcione substitua python por python3
source env/bin/activate  # Linux / macOS
env\Scripts\activate  # Windows
```

4. Instale as dependências do projeto.
```bash
pip install -r requirements.txt
```

5. Navegue até o diretório do app principal
```bash
cd social_media_app
```

6. Inicie o servidor de desenvolvimento.
```bash
python manage.py runserver # caso o comando não funcione substitua python por python3
```

7. Acesse a aplicação em seu navegador em [http://127.0.0.1:8000/.](http://127.0.0.1:8000/)

8. Para acessar a aplicação, você pode criar um novo usuário clicando no botão "Sign Up" (Registrar-se) na página inicial, caso não queira criar um novo usuário você pode usar o username 'admin' e a senha '123'.

   - Clique no botão "Sign Up" na página inicial da aplicação.
   - Preencha o formulário de registro com seu nome de usuário, endereço de e-mail e senha.
   - Clique em "Register" (Registrar) para criar sua conta.
   - Após o registro bem-sucedido, você será redirecionado para a página de login.

9. Para fazer login usando um usuário existente:

   - Na página de login, insira seu nome de usuário e senha.
   - Clique em "Login" para fazer login na aplicação.

Lembre-se de usar senhas seguras ao criar uma conta e proteger suas informações pessoais.


## Funcionalidades
   - Criar um novo usuário: Os usuários podem se registrar no aplicativo fornecendo um nome de usuário, endereço de e-mail e senha.
   - Fazer login: Os usuários registrados podem fazer login usando seu nome de usuário e senha.
   - Deslogar da conta: Os usuários podem efetuar logout de suas contas quando desejarem.
   - Visualizar o seu próprio perfil: Os usuários podem visualizar seu próprio perfil, que inclui suas publicações e a lista de pessoas que eles seguem.
   - Visualizar o perfil de outras pessoas: Os usuários podem visitar o perfil de outras pessoas para ver suas publicações e a lista de pessoas que elas seguem.
   - Editar e deletar suas próprias publicações: Os usuários têm a opção de editar ou excluir suas próprias publicações.
   - Curtir as publicações dos usuários: Os usuários podem curtir as publicações de outros usuários para expressar sua apreciação.
   - Página de busca (Browser): Os usuários podem pesquisar publicações e usuários usando a página de busca. Isso permite encontrar publicações específicas ou perfis de outros usuários.
Essas funcionalidades fornecem aos usuários uma experiência interativa e a capacidade de compartilhar, explorar e se envolver com o conteúdo e os perfis de outros usuários no aplicativo de mídia social.

## Contato
Se você tiver alguma dúvida, sugestão ou feedback, fique à vontade para entrar em contato.

   - Autor: Gabriel Rodrigues Machado
   - Email: gabrm123@gmail.com

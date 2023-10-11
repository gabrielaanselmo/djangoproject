# Projeto - Django 🌐

Este projeto é uma plataforma simples e eficaz que permite aos usuários fazer inscrições para receber newsletters e também compartilhar seus depoimentos. Através de uma interface amigável, os visitantes podem se inscrever fornecendo seus e-mails e, adicionalmente, têm a opção de deixar um depoimento sobre suas experiências ou opiniões. 

## 🚀 Instalando o Projeto

Para instalar o projeto, siga estas etapas:

### Pré-requisitos:

Antes de começar, você precisa ter o Python e o pip instalados em sua máquina.

### Windows:

```
# Clone o repositório
git clone https://github.com/gabrielaanselmo/djangoproject
cd djangoproject

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
.\venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate
```

## ☕ Usando o Projeto
Para usar o projeto, siga estas etapas:
```
# Ative o ambiente virtual (se ainda não estiver ativado)
.\venv\Scripts\activate   # No Windows

# Inicie o servidor de desenvolvimento
python manage.py runserver
```
Criando um superusuário:
```
# Execute o seguinte comando
python manage.py createsuperuser
```
Você será solicitado a inserir um nome de usuário, endereço de e-mail e senha. Com isso, este usuário terá acesso a todas as funcionalidades do painel administrativo.

Agora, abra seu navegador e acesse http://127.0.0.1:8000/ e http://127.0.0.1:8000/admin/ para ver o projeto em ação!

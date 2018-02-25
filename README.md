# Desafio da empresa Storm Security para a vaga de Desenvolvedor Backend 

# instalar o python 3.5
```sh
sudo apt-get install python3.5
```

# instalar o pip
```sh
sudo apt-get install python-pip
```

# Criar uma pasta para os arquivos do projeto e entrar nela
```sh
mkdir desafioStorm
cd desafioStorm
```

# Copiar o projeto para o diretorio que foi criado

# instalar o python-virtualenv
```sh
sudo apt-get install python-virtualenv
```

# Criar o virtualenv do projeto usando o python 3.5
```sh
virtualenv virtual -p python3.5
```

# PARA TESTAR O PROJETO

```sh
source virtual/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

# Iniciar o servidor web
```sh
python manage.py runserver
```

# Site: http://127.0.0.1:8000/

# Admin: http://127.0.0.1:8000/admin/
# Usuário: admin / Senha: 123mudar

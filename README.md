# Desafio da empresa Storm Security para a vaga de Desenvolvedor Backend

Projeto desenvolvido por Flavio Gomes Antunes.

## Criando o ambiente do projeto

### Instalar o python 3.5
```
sudo apt-get install python3.5
```

### Instalar o pip
```
sudo apt-get install python-pip
```

### Criar uma pasta para os arquivos do projeto e entrar nela
```
mkdir desafioStorm
cd desafioStorm
```

### Copiar o projeto para o diretorio que foi criado

### Instalar o python-virtualenv
```
sudo apt-get install python-virtualenv
```

### Criar o virtualenv do projeto usando o python 3.5
```
virtualenv virtual -p python3.5
```

## PARA TESTAR O PROJETO
```
source virtual/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

## Iniciar o servidor web
```
python manage.py runserver
```

## Informações de acesso

### Site: http://127.0.0.1:8000/
### Admin: http://127.0.0.1:8000/admin/
#### Usuário: admin / Senha: 123mudar
### APIs: http://127.0.0.1:8000/api/

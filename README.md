# Mython
Um CRUD completo feito em Python 3 e MySQL.

# Pré-requisitos
- **python3** – Interpretador da linguagem Python 3.
- **pip** – Sistema de gerenciamento de pacotes para o Python. 
- **mysql** – O driver do SGBD MySQL para o Python.
  
  ```shell
  python3 -m pip install mysql-connector-python # Instalação do driver.
  ```
  
# Rodando o projeto

```shell
# Executa o script de criação de um novo usuário.
python3 create.py
```
![Screenshot from 2021-11-21 14-16-12](https://user-images.githubusercontent.com/49795183/142772178-fcd175db-32c1-4c2c-b176-c5078c3fb0ea.png)
![Screenshot from 2021-11-21 14-25-17](https://user-images.githubusercontent.com/49795183/142772503-5bf17a25-6a7d-45b5-bc40-db6838692a0e.png)

```shell
# Executa o script de listagem dos usuários cadastrados.
python3 read.py
```
![Screenshot from 2021-11-21 14-33-52](https://user-images.githubusercontent.com/49795183/142772802-69d8bb75-85ae-4180-b48b-db84a525f15c.png)

```shell
# Executa o script de atualização de um usuário já cadastrado.
python3 update.py
```
![Screenshot from 2021-11-21 14-45-38](https://user-images.githubusercontent.com/49795183/142773156-cbc2a055-431a-4aef-bc5c-36379c6fd885.png)
![Screenshot from 2021-11-21 14-46-37](https://user-images.githubusercontent.com/49795183/142773173-3a1646d7-1037-43f0-8b72-b65279e93a47.png)

```shell
# Executa o script de remoção de um usuário cadastrado.
python3 delete.py
```
![Screenshot from 2021-11-21 15-42-10](https://user-images.githubusercontent.com/49795183/142774850-10202ade-0c4d-421d-90c0-40bd0c717639.png)

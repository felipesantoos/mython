-- Cria o banco de dados.
CREATE DATABASE teste;

-- Seleciona o banco de dados.
USE teste;

-- Cria a tabela.
CREATE TABLE users(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created DATETIME NOT NULL
);

-- Visualiza a tabela.
DESC users;

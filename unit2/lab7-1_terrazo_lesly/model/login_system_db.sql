CREATE DATABASE IF NOT EXISTS login_system_db;
USE login_system_db;

CREATE TABLE IF NOT EXISTS users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(256) NOT NULL,
    nombre VARCHAR(50) NOT NULL
);

INSERT INTO users (username, password, nombre) VALUES ('admin', 'admin123', 'Superadmin');

CREATE TABLE IF NOT EXISTS products (
    id_product INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);

INSERT INTO products (nombre, precio, stock) VALUES
('Playera Básica Blanca', 150.00, 40),
('Jeans Slim Fit', 599.90, 25),
('Sudadera con Capucha', 450.00, 18),
('Tenis Deportivos', 899.00, 20);
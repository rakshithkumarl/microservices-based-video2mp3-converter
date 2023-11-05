
-- CREATE USER IF NOT EXISTS 'auth_user'@'localhost' IDENTIFIED BY 'auth123';
CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'auth123'; 

CREATE DATABASE auth; 
-- CREATE DATABASE IF NOT EXISTS auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- CREATE TABLE IF NOT EXISTS user(
--     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     email VARCHAR(255) NOT NULL,
--     password VARCHAR(255) NOT NULL
-- );

INSERT INTO user (email, password) VALUES('rakshithkumar3594@gmail.com', 'admin123')
-- SQL sample file
-- demonstrating the Code Stats tool

-- Create database
CREATE DATABASE IF NOT EXISTS codestats_demo;

-- Use database
USE codestats_demo;

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create projects table
CREATE TABLE IF NOT EXISTS projects (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    language VARCHAR(50),
    lines_of_code INT DEFAULT 0,
    user_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Insert sample data
INSERT INTO users (username, email) VALUES
    ('admin', 'admin@example.com'),
    ('developer', 'dev@example.com');

INSERT INTO projects (name, description, language, lines_of_code, user_id) VALUES
    ('Code Stats', 'A code statistics tool', 'Python', 5000, 1),
    ('Web App', 'A web application', 'JavaScript', 3000, 2);

-- Query examples
SELECT * FROM users;
SELECT * FROM projects WHERE language = 'Python';
SELECT u.username, p.name FROM users u JOIN projects p ON u.id = p.user_id;
-- Script that prepares a MySQL server for the project
-- Create database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create new user hbnb_dev with a password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY  'hbnb_dev_pwd';
-- Get hbnb_dev all privileges on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Select privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

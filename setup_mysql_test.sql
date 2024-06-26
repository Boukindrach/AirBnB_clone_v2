-- Script that prepares a MySQL server for the project
-- Create database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create new user hbnb_test with a password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY  'hbnb_test_pwd';
-- Get hbnb_test all privileges on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Select privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

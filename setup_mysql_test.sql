-- This script prepares a MySQL server for the project
-- create Database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creating A new user hbnb_test (in localhost) and set password of hbnb_test to hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges on the database hbnb_test_db (and only this database)
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Grant SELECT privilege on the database performance_schema (and only this database)
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
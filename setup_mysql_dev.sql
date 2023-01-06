-- This script prepares a MySQL server for the project
-- create Database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creating A new user hbnb_dev (in localhost) and set password of hbnb_dev to hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges on the database hbnb_dev_db (and only this database)
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Grant SELECT privilege on the database performance_schema (and only this database)
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
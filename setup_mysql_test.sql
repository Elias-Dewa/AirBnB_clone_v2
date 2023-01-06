--- This script prepares a MySQL server for the project
    -- Database hbnb_test_db
    -- A new user hbnb_test (in localhost)
    -- The password of hbnb_test set to hbnb_test_pwd
    -- Grant all privileges on the database hbnb_test_db (and only this database)
    -- Grant SELECT privilege on the database performance_schema (and only this database)

CREATE DATABASE
    IF NOT EXISTS hbnb_test_db;
CREATE USER
    IF NOT EXISTS 'hbnb_test'@'localhost'
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
Grant ALL PRIVILEGES
    ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT
    ON `performance_schema`.* TO 'hbnb_test'@'localhost'
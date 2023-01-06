    --- This script prepares a MySQL server for the project
        --- Database hbnb_dev_db
        --- A new user hbnb_dev (in localhost)
        --- The password of hbnb_dev set to hbnb_dev_pwd
        --- Grant all privileges on the database hbnb_dev_db (and only this database)
        --- Grant SELECT privilege on the database performance_schema (and only this database)

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
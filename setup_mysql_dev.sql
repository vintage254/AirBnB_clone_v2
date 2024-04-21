-- creates a MYSQL server for the projects with:
--  Database hbnb_dev_db
--  User hbnb_dev with password of hbnb_dev should be set to hbnb_dev_pwd
--  Grants all privilages for hbnb_test on performance_schema
--  Grants all privilages for hbnb_dev for hbnb_dev_db

-- creates the database
-- This MySQL script prepares a MySQL server for the project.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

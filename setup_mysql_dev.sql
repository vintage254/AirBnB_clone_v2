-- creates a MYSQL server for the projects with:
--  Database hbnb_dev_db
--  User hbnb_dev with password of hbnb_dev should be set to hbnb_dev_pwd
--  Grants all privilages for hbnb_test on performance_schema
--  Grants all privilages for hbnb_dev for hbnb_dev_db

-- creates the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- A new user hbnb_dev (in localhost)
-- password of hbnb_dev should be set to hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- hbnb_dev should have all privileges on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- hbnb_dev should have SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;

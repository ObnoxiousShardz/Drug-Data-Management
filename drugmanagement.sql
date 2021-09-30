CREATE DATABASE IF NOT EXISTS drugmanagement;

USE drugmanagement;

CREATE TABLE IF NOT EXISTS drugdata
(
  
	Name VARCHAR(50),
	Manufacturer VARCHAR (50),
	Quantity INT, 
	Manufacture_Date VARCHAR(20),
	Expiry_Date VARCHAR(20),
	ID INT PRIMARY KEY AUTO_INCRIMENT
);
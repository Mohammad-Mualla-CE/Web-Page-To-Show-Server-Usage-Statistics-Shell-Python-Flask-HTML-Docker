use statisticsDB;

CREATE TABLE  memoryusage(
	Id INT NOT NULL AUTO_INCREMENT,
	time varchar(100), 
	usedm INT, 
	freem INT,
	PRIMARY KEY (Id)
);



CREATE TABLE  cpuusage(
	Id INT NOT NULL AUTO_INCREMENT,
	cpuUsage varchar(300),
	PRIMARY KEY (Id)
);


CREATE TABLE  diskusage(
	Id INT NOT NULL AUTO_INCREMENT,
	time varchar(100),
	filesystem varchar(400), 
	size varchar(400), 
	usedDisk varchar(400), 
	availableDisk varchar(400),
	PRIMARY KEY (Id)
);


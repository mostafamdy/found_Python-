show databases;
create database found;
use found;
show tables;


CREATE TABLE childnotfound (
  ChildID INT Not NULL auto_increment,
  Name varchar(50) DEFAULT NULL,
  age int(11) DEFAULT NULL,
  Description text DEFAULT NULL,
  Image text DEFAULT NULL,
  primary key(ChildID)
)
select * from childnotfound;

CREATE TABLE childfounded (
  ChildID INT not NULL auto_increment,
  Name varchar(50) DEFAULT NULL,
  Location varchar(50) DEFAULT NULL,
  age int(11) DEFAULT NULL,
  Description text DEFAULT NULL,
  Image text DEFAULT NULL,
  primary key(ChildID)
);



CREATE TABLE someOne (
  Name varchar(50) ,
  phone varchar(20) ,
  ChildID INT 
);

CREATE TABLE parent (
  Name varchar(50) DEFAULT NULL,
  NationalId varchar(50) DEFAULT NULL,
  IdPhoto varchar(50) DEFAULT NULL
);

CREATE TABLE imageTest (
  ChildID INT not NULL auto_increment,
  typ varchar(50) DEFAULT NULL,
  image varchar(50) DEFAULT NULL,
  indx varchar(50) DEFAULT NULL,
  id varchar(50) DEFAULT NULL,
  primary key(ChildID)
);
CREATE TABLE results (
  FoundID varchar(50) DEFAULT NULL,
  NotFoundID varchar(50) DEFAULT NULL
 );
 
 
 INSERT INTO childNotFound (Name , Age , Description ,Image ) VALUES("mostafa",10,"description","/static/050821155756.jpg");
 INSERT INTO childFounded (Name , Location , age , Description , Image  ) VALUES ("name", "x=5,y=5",10, "description","");
 INSERT INTO childFounded (Name , Location , age , Description , Image  ) VALUES ("amr", "x=5,y=5",10, "description","/static/050821145549.jpg");
 INSERT INTO someOne (Name , Phone ,ChildID) VALUES ( "name", "01125",1);
 INSERT INTO someOne (Name , Phone ,ChildID) VALUES ( "name", "01125",2);
 INSERT INTO parent (Name , NationalId ,IdPhoto) VALUES ( "parentName", "id622253", "");
 
select *from childfounded;
select *from childnotfound;
select *from someone;
select *from parent;
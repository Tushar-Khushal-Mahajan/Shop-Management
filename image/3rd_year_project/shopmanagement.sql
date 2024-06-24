CREATE DATABASE shopmanagement;
USE shopmanagement;

CREATE TABLE shop(
	sh_id int primary key,
    sh_name varchar(30) not null, 
    sh_status varchar(5),
    mono varchar(12) not null check(length(mono) >= 10),
    pass varchar(20) not null,
    check(sh_status='yes' or sh_status='no'),
    unique(sh_name, mono)
);
select *from shop;
drop table shop;
truncate table shop;

insert into shop values(1,'tushant electronicks','yes','8637729558','tushant123');
insert into shop values(2, 'sai ele','no','1234567890','123');

CREATE DATABASE shopmanagement;
USE shopmanagement;

drop database shopmanagement;

CREATE TABLE shop(
	sh_id int primary key auto_increment,
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

set sql_safe_updates=0;
update shop set sh_status='no' where sh_id=1;
update shop set sh_status='yes' where sh_status='no';
update shop set sh_status='yes' where sh_id=1;
delete from shop where sh_id = 2;

insert into shop(sh_name,sh_status,mono,pass) values('tushant electronicks','yes','8637729558','tushant123');
insert into shop values(2, 'sai ele','no','1234567890','123');



/* ========================================  products table ===============================================*/

create table products(
						sh_id int,
						p_id int primary key AUTO_INCREMENT,
						p_name varchar(30) unique not null,
						p_qty int,
						p_price double not null,
						s_price double not null,
                        foreign key(sh_id) references shop(sh_id)
					 );
alter table products AUTO_INCREMENT=101;


insert into products(sh_id,p_name,p_qty,p_price,s_price) values(1,"AA cell",20,10,15);

SELECT p_id from products WHERE sh_id=1 order by p_id desc;


drop table products;
					
select *from products;
select *from shop;

truncate table products;

SELECT p_price FROM products WHERE p_id=101 AND sh_id=1;

delete from products where sh_id =1;

insert into products(sh_id, p_name,p_qty,p_price,s_price) values(2,'solar banner',20,700,1000);


SELECT p_id,p_name,p_qty,s_price,count(p_name)as count FROM products WHERE p_name like '%i%' AND sh_id = 1 group by  p_id,p_name,p_qty,s_price;
SELECT count(p_name)as count FROM products WHERE p_name like '%i%' AND sh_id = 1;
        



/*==========================================uniqye selling id==========================================*/
create table sell_id(
						s_id int primary key AUTO_INCREMENT,
						abc varchar(10)
					);
alter table sell_id AUTO_INCREMENT=1000;
select *from sell_id;

drop table sell_id;



/*========================================= temporary selling table for treeview ================================*/

create table selling_table (
								sh_id int,
								s_id int,  /*value automatic fill in a python program*/
								p_name varchar(30) ,
								qty int,
								p_price double,
								s_price double,
								total_price double,
								date datetime,
								p_id int,
                                primary key(s_id,p_id),
                                foreign key(p_id) references products(p_id)
						   );
select *from selling_table;


delete from sell_id where s_id not in (select s_id from selling_table);

drop table selling_table;

truncate table selling_table;

delete from selling_table;

truncate table selling_table;

/*================================================================= confirm sell ================================================================*/
create table confirm_selling (
								sh_id int,
								s_id int unique , /*value automatic fill in a python program*/
                                s_date datetime,
                                foreign key (s_id) references selling_table(s_id)
						   );
select *from confirm_selling;

insert into confirm_selling(sh_id,s_id,s_date) VALUES(1,1002,'23-01-19');
-- delete from selling_table where s_id not in (select s_id from confirm_selling);
-- delete from sell_id where s_id not in(select s_id from confirm_selling);


drop table confirm_selling;
drop table selling_table;
drop table sell_id;








select *from sell_id;
select *from selling_table;
select *from confirm_selling; 







/*========================================= CREADIT =========================================*/

create table creadit(	
						sh_id int,
                        s_id int unique,
                        c_name varchar(20),
                        c_city varchar(10),
						mo_no varchar(15)  check(mo_no >= 10),
						total int,
                        creadit int,
                        date datetime,
                        rem_date datetime,
                        foreign key(s_id) references confirm_selling(s_id)
					);
select *from creadit;

select count(s_id) from creadit where mo_no = 7558489136;

select s_id from creadit where '2023-01-19 00:00:00' in (select rem_date from creadit);

delete from  creadit where s_id < 1009;

drop table creadit;

select datediff('2023,01,18','2023-01-19');  -- (old_date, new_date); 






/*===================================================== temporary order table ============================================*/ 

create table orders(
	sh_id int references shop(sh_id),
    p_id int,
	o_id int not null,
    p_name varchar(30),
    o_qty int,
    unique(p_name,o_id)
);

insert into orders values(1,1,'2 pin top',2);

select *from orders;
delete from orders where p_id=0;

update orders set o_qty= o_qty+10 where p_id=101 and sh_id=1 and o_id=1;

truncate table orders;
select *from products;
drop table orders;


create table receive_orders(
								sh_id int,
                                o_id int references orders(o_id),
                                supplier varchar(30),
                                receive_date date
							);

select *from receive_orders;

truncate table receive_orders;

drop table receive_orders;
insert into receive_orders values(101,'tushar','03-12-2023');

-- ------------------------------------------------------------------------------------
SELECT p_id,p_name FROM products where sh_id='1' and p_qty>='11' AND p_qty<='20' order by p_qty asc;

SELECT p_id,p_name FROM products where sh_id='1' and p_id not in(select p_id from orders where sh_id='1' AND o_id='1') and p_qty>='11' AND p_qty<='20' order by p_qty asc



select p_id,p_name,p_qty,s_price from products as a where sh_id = 1
union select p_id,p_name,"","" from orders as b where b.p_id not in(select p_id from products where sh_id=1) AND b.o_id='1' AND b.sh_id=1;

select count(a.p_name) from products as a where sh_id = 1
union select count(b.p_name) from orders as b where b.p_id not in(select p_id from products where sh_id=1) AND b.o_id='1' AND b.sh_id=1;

select p_id,p_name,p_qty,s_price from products as a where sh_id = '1' AND p_name like '%2pin%' 
union select p_id,p_name,"","" from orders as b where b.p_id not in(select p_id from products where sh_id=1) AND b.o_id='1' AND b.sh_id=1 AND b.p_name like '%2pin%' ;
-- -----------------------------------------------------------------------------------


drop table orders;


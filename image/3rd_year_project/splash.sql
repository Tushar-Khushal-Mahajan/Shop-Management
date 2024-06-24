create database splash;
use splash;


create table shop(
					sh_id int not null,
					shop_name varchar(30) not null,
					shop_status varchar(5) check(shop_status='yes' or shop_status='no'),
					shop_pass nvarchar(20) unique not null,
					primary key(sh_id)
				 );
alter table shop drop constraint [UQ__shop__D9D3EA0CE904772A]

insert into shop values(1,'tushant electronicks','yes','tushant123')
insert into shop values(2, 'sai ele','no','123')
insert into shop values(3, 'om ele','no','456')
insert into shop values(4,'shree ele','no','789')
insert into shop values(5, 'my ele','no','101')
insert into shop values(6, 'two ele','no','102')

select *from shop;
update shop set shop_status='no' where sh_id=1
update shop set shop_status='no' where sh_id <= (select max(sh_id) from shop)
update shop set shop_status='yes' where sh_id=4;

delete shop where sh_id=9012

drop table shop;

/*============================= products table ==========================*/
create table products(
						sh_id int references shop(sh_id),
						p_id int primary key identity(101,1),
						p_name varchar(30) unique not null,
						p_qty int,
						p_price money not null,
						s_price money not null
					 );

					 drop table products;
select *from products;

truncate table products

drop table products
/*==========================================uniqye selling id==========================================*/
create table sell_id(
						s_id int primary key identity(10000,1),
						abc varchar(10)
					);
select *from sell_id
insert into sell_id values('abc');
drop table sell_id
/*========================================= selling table ================================*/

create table selling_table (
								sh_id int,
								s_id int primary key,
								p_name varchar(30),
								qty int,
								p_price money,
								s_price money,
								total_price money,
								date datetime,
								p_id int references products(p_id)
						   );

select *from selling_table


truncate table selling_table

drop table selling_table


delete selling_table where sh_id = 1

insert into selling_table values(2,1011,'abc',1,8,10,10,'2022-07-26',101)


drop database shop

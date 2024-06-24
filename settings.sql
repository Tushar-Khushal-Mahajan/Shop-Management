create database datasetting;
use datasetting;

create table order_ws(
		sh_id int,
        l_stock_qty int,
        m_stock_qty int,
        saving_path varchar(100)
);

truncate table order_ws;

UPDATE order_ws SET l_stock_qty="30", m_stock_qty="20", saving_path='c:/shop management/order_recipts/' WHERE sh_id=1;

select *from order_ws;

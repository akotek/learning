# simple mysql-cheatsheet

--show full processlist;
show full processlist;

--table_def
SHOW CREATE TABLE mytable;

--add colX after colY
ALTER TABLE table ADD colX AFTER colY

--update_row
UPDATE table_name SET field1=new_val where..
--error 1175: 
SET SQL_SAFE_UPDATES = 0; *CHANGE*, SET SQL_SAFE_UPDATES = 1;

--remove row
DELETE FROM products WHERE product_id=1;

--remove_col
ALTER TABLE tbl_Country DROP COLUMN IsDeleted;

--to delete table with FK
SET FOREIGN_KEY_CHECKS=0;
drop table if exists....
SET FOREIGN_KEY_CHECKS=1;

--see views
SHOW FULL TABLES IN sproutt WHERE TABLE_TYPE LIKE 'VIEW';

--get-mysql-configs
/usr/local/bin/mysqld --verbose --help | grep -A 1 "Default options";  

--auto-inc-reset
ALTER TABLE tableName AUTO_INCREMENT = 1;

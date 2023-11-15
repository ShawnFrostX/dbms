CREATE TABLE `try2`.`activity` (
  `act_id` INT NOT NULL,
  `act_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`act_id`));
  
  CREATE TABLE `try2`.`place` (
  `act_id` INT NOT NULL,
  `place` VARCHAR(45) NOT NULL,
  `district` VARCHAR(45) NOT NULL);
  
  alter table place add foreign key(act_id) references activity(act_id) on delete cascade ;
  
  CREATE TABLE `try2`.`shop` (
  `item_id` INT NOT NULL,
  `shop` VARCHAR(100) NULL,
  `shop_id` INT NULL,
  `price` INT NULL);

alter table shop add foreign key(item_id) references item(item_id) on delete cascade ;

CREATE TABLE `try2`.`item` (
  `act_id` INT NOT NULL,
  `item_id` INT NOT NULL,
  `item` VARCHAR(45) NULL,
  PRIMARY KEY (`item_id`));

alter table item add foreign key(act_id) references activity(act_id) on delete cascade ;
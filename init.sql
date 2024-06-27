CREATE SCHEMA `task_manager` ;
CREATE TABLE `task_manager`.`tasks` (
  `description` VARCHAR(45) NOT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  `status` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));
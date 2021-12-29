-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema bankingbot
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bankingbot
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bankingbot` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`user` (
  `username` VARCHAR(16) NOT NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(32) NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP);

USE `bankingbot` ;

-- -----------------------------------------------------
-- Table `bankingbot`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bankingbot`.`user` (
  `email` VARCHAR(100) NULL DEFAULT NULL,
  `password` VARCHAR(40) NULL DEFAULT NULL,
  `phone` VARCHAR(50) NULL DEFAULT NULL,
  `name` VARCHAR(40) NULL DEFAULT NULL,
  `user_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bankingbot`.`account`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bankingbot`.`account` (
  `account_no` VARCHAR(15) NOT NULL,
  `user_id` INT NULL DEFAULT NULL,
  `bank_name` VARCHAR(500) NULL DEFAULT NULL,
  `Branch_address` VARCHAR(500) NULL DEFAULT NULL,
  PRIMARY KEY (`account_no`),
  INDEX `fk_1` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_1`
    FOREIGN KEY (`user_id`)
    REFERENCES `bankingbot`.`user` (`user_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bankingbot`.`benificiary`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bankingbot`.`benificiary` (
  `benificiary_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NULL DEFAULT NULL,
  `ben_name` VARCHAR(50) NULL DEFAULT NULL,
  `ben_mail` VARCHAR(50) NULL DEFAULT NULL,
  `ben_number` VARCHAR(15) NULL DEFAULT NULL,
  `account_no` VARCHAR(15) NULL DEFAULT NULL,
  PRIMARY KEY (`benificiary_id`),
  INDEX `fk_4` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_4`
    FOREIGN KEY (`user_id`)
    REFERENCES `bankingbot`.`user` (`user_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bankingbot`.`card`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bankingbot`.`card` (
  `card_no` VARCHAR(15) NOT NULL,
  `user_id` INT NULL DEFAULT NULL,
  `card_type` VARCHAR(20) NULL DEFAULT NULL,
  `card_name` VARCHAR(300) NULL DEFAULT NULL,
  `issued_date` DATE NULL DEFAULT NULL,
  `expiry_date` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`card_no`),
  INDEX `fk_3` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_3`
    FOREIGN KEY (`user_id`)
    REFERENCES `bankingbot`.`user` (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `bankingbot`.`transactions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bankingbot`.`transactions` (
  `transaction_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NULL DEFAULT NULL,
  `transaction_date` DATE NULL DEFAULT NULL,
  `from_account` VARCHAR(15) NULL DEFAULT NULL,
  `to_account` VARCHAR(15) NULL DEFAULT NULL,
  `amount` INT NULL DEFAULT NULL,
  PRIMARY KEY (`transaction_id`),
  INDEX `fk_2` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_2`
    FOREIGN KEY (`user_id`)
    REFERENCES `bankingbot`.`user` (`user_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

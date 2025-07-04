/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.4.32-MariaDB : Database - hostel
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`hostel` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `hostel`;

/*Table structure for table `application` */

DROP TABLE IF EXISTS `application`;

CREATE TABLE `application` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `mobile` int(11) NOT NULL,
  `hosteltype` varchar(50) NOT NULL,
  `hostelname` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `date_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback` text NOT NULL,
  `mail` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Table structure for table `hosteldetails` */

DROP TABLE IF EXISTS `hosteldetails`;

CREATE TABLE `hosteldetails` (
  `hostel_id` int(100) NOT NULL AUTO_INCREMENT,
  `Hostelname` varchar(100) DEFAULT NULL,
  `AC_rooms` varchar(100) DEFAULT NULL,
  `NonACrooms` varchar(100) DEFAULT NULL,
  `Roomsharing` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `ACroomfees` varchar(100) DEFAULT NULL,
  `Non_ACroomfees` varchar(100) DEFAULT NULL,
  `AC_roomvacancy` varchar(100) DEFAULT NULL,
  `Non_AC_roomvacancy` varchar(100) DEFAULT NULL,
  `contact_no` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`hostel_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `uid` varchar(50) DEFAULT NULL,
  `un` varchar(50) DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `mn` varchar(50) DEFAULT NULL,
  `ht` varchar(50) DEFAULT NULL,
  `hn` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `cardnumber` varchar(50) DEFAULT NULL,
  `cvv` varchar(50) DEFAULT NULL,
  `todaysdate` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT 'accepted',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `address` varchar(100) NOT NULL,
  `status` varchar(40) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Table structure for table `vacate` */

DROP TABLE IF EXISTS `vacate`;

CREATE TABLE `vacate` (
  `Username` varchar(50) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `hostelname` varchar(50) NOT NULL,
  `vacatestatus` varchar(50) NOT NULL,
  `reason` varchar(50) NOT NULL,
  `date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

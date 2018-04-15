-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 22, 2014 at 09:10 PM
-- Server version: 5.5.40-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `pythondb2`
--

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE IF NOT EXISTS `answers` (
  `user` varchar(9) NOT NULL DEFAULT '',
  `selection` text,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `answers`
--

INSERT INTO `answers` (`user`, `selection`) VALUES
('COE12B013', '3-3,4-3,16-1,21-2,26--1,27-1,29-1,30-2'),
('COE12B021', '3-3,4-2,16-2,21--1,26-1,27--1,29-1,30-3');

-- --------------------------------------------------------

--
-- Table structure for table `Qpaper2`
--

CREATE TABLE IF NOT EXISTS `Qpaper2` (
  `qId` int(11) NOT NULL DEFAULT '0',
  `question` text,
  `opt1` text,
  `opt2` text,
  `opt3` text,
  `opt4` text,
  PRIMARY KEY (`qId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Qpaper2`
--

INSERT INTO `Qpaper2` (`qId`, `question`, `opt1`, `opt2`, `opt3`, `opt4`) VALUES
(1, 'Which one of these is a network topology?', 'CAR', 'TRAIN', 'BUS', 'VAN'),
(3, 'Which one of the following is a function of network layer?', 'Digestion Control', 'Congestion Control', 'Mission Control', 'Control-C'),
(6, 'Which one of these is an Operating System?', 'OS-X Leopard', 'Windows and Doors 7', 'OS-X Dosa', 'Windows IDLI'),
(7, 'Who invented Windows?', 'India Gate', 'Bill Gates', 'Arnab Goswami', 'Narendra Modi'),
(12, 'What is Perl?', 'It is a snake', 'It is a Scripting Language', 'It is an expensive ornament', 'It is a type of Dosa'),
(13, 'Who invented Python?', 'Pruthvi Nagalla', 'Praneeth Cool', 'Guido van Rossum', 'Kishore Kalyan'),
(15, 'What is javascript?', 'It is a web development language?', 'Mother of Java', 'Sister of Java', 'Brother of Java'),
(16, 'Which of these is a model in software development?', 'Hari Krishna', 'Angelina Jolie', 'Waterfall Model', 'Arjun Rampal'),
(18, 'In Virtual Reality which of these senses cannot be potrayed?', 'Smell', 'Sight', 'Touch', 'Hearing');

-- --------------------------------------------------------

--
-- Table structure for table `quesPaper`
--

CREATE TABLE IF NOT EXISTS `quesPaper` (
  `qId` int(11) NOT NULL,
  `question` text NOT NULL,
  `opt1` text,
  `opt2` text,
  `opt3` text,
  `opt4` text,
  PRIMARY KEY (`qId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Question5`
--

CREATE TABLE IF NOT EXISTS `Question5` (
  `qId` int(11) NOT NULL DEFAULT '0',
  `question` text,
  `opt1` text,
  `opt2` text,
  `opt3` text,
  `opt4` text,
  PRIMARY KEY (`qId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Question5`
--

INSERT INTO `Question5` (`qId`, `question`, `opt1`, `opt2`, `opt3`, `opt4`) VALUES
(1, 'Which one of these is a network topology?', 'CAR', 'TRAIN', 'BUS', 'VAN'),
(3, 'Which one of the following is a function of network layer?', 'Digestion Control', 'Congestion Control', 'Mission Control', 'Control-C'),
(4, 'The 4 byte IP address consists of ?', 'Network Address & Host Address', 'Presidents Address & Prime Ministers Address', 'My Address & Your Address', 'No Address'),
(5, 'The network layer protocol of the internet is?', 'Mission Impossible IV Ghost Protocol', 'Internet Protocol', 'Pythagoras Protocol', 'There is no Protocol'),
(7, 'Who invented Windows?', 'India Gate', 'Bill Gates', 'Arnab Goswami', 'Narendra Modi'),
(9, 'What is the full form of OS?', 'Organising System', 'Original Syntax', 'Om Shanthi Om', 'Operating System'),
(11, 'Which one of these is a Python GUI package?', 'Tkinter', 'Kinder Joy', 'Kinder Suprise', 'Terminator'),
(12, 'What is Perl?', 'It is a snake', 'It is a Scripting Language', 'It is an expensive ornament', 'It is a type of Dosa'),
(14, 'What is mySQL?', 'Is it a database', 'It is a subatomic particle', 'It is a hill station in Ooty', 'It is the main ingredient of Sambar'),
(16, 'Which of these is a model in software development?', 'Hari Krishna', 'Angelina Jolie', 'Waterfall Model', 'Arjun Rampal'),
(17, 'Which of these languages are read from left to right?', 'Arabic', 'English', 'Hindi', 'Telugu'),
(18, 'In Virtual Reality which of these senses cannot be potrayed?', 'Smell', 'Sight', 'Touch', 'Hearing');

-- --------------------------------------------------------

--
-- Table structure for table `QuestionPaper3`
--

CREATE TABLE IF NOT EXISTS `QuestionPaper3` (
  `qId` int(11) NOT NULL DEFAULT '0',
  `question` text,
  `opt1` text,
  `opt2` text,
  `opt3` text,
  `opt4` text,
  PRIMARY KEY (`qId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `QuestionPaper3`
--

INSERT INTO `QuestionPaper3` (`qId`, `question`, `opt1`, `opt2`, `opt3`, `opt4`) VALUES
(1, 'Which one of these is a network topology?', 'CAR', 'TRAIN', 'BUS', 'VAN'),
(2, 'The Network layer concerns with which one of these?', 'Juice Packet', 'Biscuit Packet', 'Aata Packet', 'Data Packet'),
(3, 'Which one of the following is a function of network layer?', 'Digestion Control', 'Congestion Control', 'Mission Control', 'Control-C'),
(5, 'The network layer protocol of the internet is?', 'Mission Impossible IV Ghost Protocol', 'Internet Protocol', 'Pythagoras Protocol', 'There is no Protocol'),
(6, 'Which one of these is an Operating System?', 'OS-X Leopard', 'Windows and Doors 7', 'OS-X Dosa', 'Windows IDLI'),
(7, 'Who invented Windows?', 'India Gate', 'Bill Gates', 'Arnab Goswami', 'Narendra Modi'),
(9, 'What is the full form of OS?', 'Organising System', 'Original Syntax', 'Om Shanthi Om', 'Operating System'),
(10, 'Which one of these is a scripting language?', 'Python', 'Cobra', 'Rat Snake', 'Hari Krishna'),
(11, 'Which one of these is a Python GUI package?', 'Tkinter', 'Kinder Joy', 'Kinder Suprise', 'Terminator'),
(12, 'What is Perl?', 'It is a snake', 'It is a Scripting Language', 'It is an expensive ornament', 'It is a type of Dosa'),
(14, 'What is mySQL?', 'Is it a database', 'It is a subatomic particle', 'It is a hill station in Ooty', 'It is the main ingredient of Sambar'),
(15, 'What is javascript?', 'It is a web development language?', 'Mother of Java', 'Sister of Java', 'Brother of Java'),
(17, 'Which of these languages are read from left to right?', 'Arabic', 'English', 'Hindi', 'Telugu'),
(19, 'Which one of these is a factor in HCI? ', 'Temperature', 'Usability', 'Rain', 'Earthquake');

-- --------------------------------------------------------

--
-- Table structure for table `selections`
--

CREATE TABLE IF NOT EXISTS `selections` (
  `userId` varchar(9) NOT NULL DEFAULT '',
  `selection` text NOT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

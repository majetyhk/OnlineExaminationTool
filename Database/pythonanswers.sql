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
-- Database: `pythonanswers`
--

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE IF NOT EXISTS `answers` (
  `user` varchar(9) NOT NULL DEFAULT '',
  `selection` text,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Qpaper2`
--

CREATE TABLE IF NOT EXISTS `Qpaper2` (
  `user` varchar(9) NOT NULL DEFAULT '',
  `selection` text,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Qpaper2`
--

INSERT INTO `Qpaper2` (`user`, `selection`) VALUES
('COE12B002', '1,3;3,4;6,1;7,2;12,2;13,2;15,1;16,3;18,1');

-- --------------------------------------------------------

--
-- Table structure for table `quesPaper`
--

CREATE TABLE IF NOT EXISTS `quesPaper` (
  `user` varchar(9) NOT NULL DEFAULT '',
  `selection` text,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `quesPaper`
--

INSERT INTO `quesPaper` (`user`, `selection`) VALUES
('COE12B001', '3,-1;4,-1;16,-1;21,-1;26,-1;27,-1;29,-1;30,-1'),
('COE12B002', '3,-1;4,-1;16,-1;21,-1;26,-1;27,-1;29,-1;30,-1'),
('COE12B003', '3,-1;4,-1;16,-1;21,-1;26,-1;27,-1;29,-1;30,-1'),
('COE12B005', '3,-1;4,-1;16,-1;21,-1;26,-1;27,-1;29,-1;30,-1'),
('COE12B012', '3,-1;4,-1;16,-1;21,-1;26,-1;27,-1;29,-1;30,-1'),
('COE12B017', '3,-1;4,-1;16,-1;21,-1;26,-1;27,-1;29,-1;30,-1');

-- --------------------------------------------------------

--
-- Table structure for table `QuestionPaper3`
--

CREATE TABLE IF NOT EXISTS `QuestionPaper3` (
  `user` varchar(9) NOT NULL DEFAULT '',
  `selection` text,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `QuestionPaper3`
--

INSERT INTO `QuestionPaper3` (`user`, `selection`) VALUES
('COE12B017', '1,3;2,4;3,3;5,4;6,1;7,2;9,4;10,3;11,1;12,2;14,1;15,1;17,1;19,2');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

/*
Navicat MySQL Data Transfer

Source Server         : web
Source Server Version : 50630
Source Host           : localhost:3306
Source Database       : web_pokemon

Target Server Type    : MYSQL
Target Server Version : 50630
File Encoding         : 65001

Date: 2016-12-06 19:09:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `post`
-- ----------------------------
DROP TABLE IF EXISTS `post`;
CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author` varchar(50) NOT NULL,
  `content` char(255) NOT NULL,
  `date` datetime NOT NULL,
  `likes` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of post
-- ----------------------------
INSERT INTO `post` VALUES ('1', '2', 'hahahaha', '2016-11-29 13:45:10', '17');
INSERT INTO `post` VALUES ('2', '2', 'testt', '2016-11-29 13:45:49', '0');
INSERT INTO `post` VALUES ('3', 'wer', 'hi', '2016-11-29 14:22:55', '0');
INSERT INTO `post` VALUES ('4', 'gypdtc01', 'hahahaha', '2016-11-29 14:26:49', '1');
INSERT INTO `post` VALUES ('5', 'gypdtc01', 'hahahah2', '2016-11-29 14:26:56', '3');
INSERT INTO `post` VALUES ('6', '2', 'sadasd', '2016-11-29 14:38:11', '0');

-- ----------------------------
-- Table structure for `user_account`
-- ----------------------------
DROP TABLE IF EXISTS `user_account`;
CREATE TABLE `user_account` (
  `user_ID` varchar(255) NOT NULL,
  `salt` varchar(255) NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 NOT NULL,
  `nickname` varchar(255) CHARACTER SET utf8 NOT NULL,
  `ID` int(255) unsigned NOT NULL AUTO_INCREMENT,
  `email_address` varchar(255) DEFAULT NULL,
  `team` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user_account
-- ----------------------------
INSERT INTO `user_account` VALUES ('1', '1', '1', '1', '1', null, '');
INSERT INTO `user_account` VALUES ('aaa', '2016-10-13 00:47:48.933000', 'f04c68430b1120466a996844c56d6c93', '2012016', '2', null, 'undecide');
INSERT INTO `user_account` VALUES ('\r\naaa', '2016-10-13 00:47:48.933000', 'f04c68430b1120466a996844c56d6c93', '2012016', '3', null, '');
INSERT INTO `user_account` VALUES ('gypdtc', '2016-10-13 01:31:48.269000', '9c3270c66f14ff80dff9d5534448c6b5', '1', '7', null, '');
INSERT INTO `user_account` VALUES ('2', '2016-11-29 15:46:26.127000', 'fc9f1cdae7847a89052b24c54c856a30', '2', '9', '123123', '');
INSERT INTO `user_account` VALUES ('qwe', '2016-12-06 02:09:01.357000', '046f6a54d0b29b01eb64e7298dbc0070', 'qwe', '48', 'qwe', 'undecide');
INSERT INTO `user_account` VALUES ('123', '2016-12-06 03:50:24.502000', '28f7cad132f2d850538881209aa26a43', '1234', '50', '123', 'mystic');
INSERT INTO `user_account` VALUES ('asd', '2016-12-06 12:11:06.665000', '6f89534825ac1d9bbcbc4b42b6c191bb', 'asd', '51', 'asd', 'undecide');
INSERT INTO `user_account` VALUES ('assdf', '2016-12-06 12:11:17.022000', '90d56e5f939a3bd9cbfdd15c529bfdd5', 'asdf', '52', 'asdf', 'instinct');
INSERT INTO `user_account` VALUES ('assdfe', '2016-12-06 12:11:30.521000', 'c3154d39ec597d2360890edab9d32b47', 'asdfe', '53', 'asdfe', 'valor');

-- ----------------------------
-- Table structure for `user_follow`
-- ----------------------------
DROP TABLE IF EXISTS `user_follow`;
CREATE TABLE `user_follow` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `user_follower` int(11) unsigned NOT NULL,
  `user_followed` int(11) unsigned NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `USER_ID` (`user_follower`),
  KEY `Follow_ID` (`user_followed`),
  CONSTRAINT `user_follow_ibfk_1` FOREIGN KEY (`user_follower`) REFERENCES `user_account` (`ID`),
  CONSTRAINT `user_follow_ibfk_2` FOREIGN KEY (`user_followed`) REFERENCES `user_account` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user_follow
-- ----------------------------
INSERT INTO `user_follow` VALUES ('12', '50', '2');
INSERT INTO `user_follow` VALUES ('14', '50', '53');
INSERT INTO `user_follow` VALUES ('15', '50', '52');

-- ----------------------------
-- Table structure for `user_post`
-- ----------------------------
DROP TABLE IF EXISTS `user_post`;
CREATE TABLE `user_post` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `User_ID` int(11) unsigned zerofill NOT NULL,
  `Date` datetime NOT NULL,
  `type` char(255) NOT NULL,
  `content` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `User_ID` (`User_ID`),
  CONSTRAINT `user_post_ibfk_1` FOREIGN KEY (`User_ID`) REFERENCES `user_account` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user_post
-- ----------------------------
INSERT INTO `user_post` VALUES ('1', '00000000009', '2016-11-26 23:58:21', '1', 'dsdasdada');

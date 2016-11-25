/*
Navicat MySQL Data Transfer

Source Server         : web
Source Server Version : 50630
Source Host           : localhost:3306
Source Database       : web_pokemon

Target Server Type    : MYSQL
Target Server Version : 50630
File Encoding         : 65001

Date: 2016-10-31 21:43:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `user_account`
-- ----------------------------
DROP TABLE IF EXISTS `user_account`;
CREATE TABLE `user_account` (
  `user_ID` varchar(255) NOT NULL,
  `salt` varchar(255) NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 NOT NULL,
  `nickname` varchar(255) CHARACTER SET utf8 NOT NULL,
  `ID` int(255) NOT NULL AUTO_INCREMENT,
  `email_address` varchar(255) DEFAULT NULL,
  `team` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user_account
-- ----------------------------
INSERT INTO `user_account` VALUES ('1', '1', '1', '1', '1', null, '');
INSERT INTO `user_account` VALUES ('aaa', '2016-10-13 00:47:48.933000', 'f04c68430b1120466a996844c56d6c93', '2012016', '2', null, '');
INSERT INTO `user_account` VALUES ('\r\naaa', '2016-10-13 00:47:48.933000', 'f04c68430b1120466a996844c56d6c93', '2012016', '3', null, '');
INSERT INTO `user_account` VALUES ('gypdtc', '2016-10-13 01:31:48.269000', '9c3270c66f14ff80dff9d5534448c6b5', '1', '7', null, '');
INSERT INTO `user_account` VALUES ('2', '2016-10-13 01:35:13.983000', '14ffc12c61960b5a4755d1a18b7ba9ca', '2', '9', null, '');
INSERT INTO `user_account` VALUES ('3', '2016-10-13 12:51:24.726000', '9af16d339b1e5531a4c0778785479e76', '3', '10', null, '');
INSERT INTO `user_account` VALUES ('5', '2016-10-13 12:54:37.944000', '04c50a5a61bfc118d292725abc2ff0be', '5', '11', null, '');
INSERT INTO `user_account` VALUES ('6', '2016-10-13 13:02:57.216000', '289eb6711c2bcd1db0bc227dcb407da0', '6', '12', null, '');
INSERT INTO `user_account` VALUES ('11', '2016-10-13 13:20:00.909000', '891a159b8aa93f8b3ebf6f7accf048ec', '11', '13', null, '');
INSERT INTO `user_account` VALUES ('123', '2016-10-13 13:33:03.608000', '056bf1d0eded3b5c12f711ed6b26b285', '123', '14', null, '');
INSERT INTO `user_account` VALUES ('111111', '2016-10-13 17:05:46.470000', 'b8b2b73b6e70060fa2c680e7490d05d4', '11', '15', null, '');
INSERT INTO `user_account` VALUES ('10', '2016-10-13 17:18:49.249000', '17869152998afb20565ca609c1a4f7ad', '10', '16', null, '');
INSERT INTO `user_account` VALUES ('00', '2016-10-14 21:38:52.280000', '0457bac43486613f03d9954aea7e8f15', '00', '17', null, '');
INSERT INTO `user_account` VALUES ('12', '2016-10-14 21:43:59.444000', '30d0e621011130a1a6d0f036295fdab2', '12', '18', '12', 'valor');
INSERT INTO `user_account` VALUES ('12312', '2016-10-15 00:38:10.557000', 'a06f8d0bd309f10ca161fce3a05db736', '123123', '19', '131231', 'mystic');
INSERT INTO `user_account` VALUES ('t1', '2016-10-23 18:11:07.750000', '0611ae5dbaddf0d30f9771be23344470', 't1', '20', 't1', 'mystic');
INSERT INTO `user_account` VALUES ('x', '2016-10-24 00:33:45.457000', 'dc53e5306b983adc252f5169390c746e', 'x', '21', 'x', 'undecide');
INSERT INTO `user_account` VALUES ('r', '2016-10-24 00:34:23.130000', 'dd6bbba8b2c924361779c8b2e03a41ac', 'r', '22', 'r', 'valor');
INSERT INTO `user_account` VALUES ('f1', '2016-10-24 00:36:31.956000', '93f3253a201d12395dc56e12a25a0e3e', 'f1', '23', 'f1', 'instinct');
INSERT INTO `user_account` VALUES ('honglin', '2016-10-24 20:08:05.713000', 'c1e857a1848872b95860a62685deb29e', 'honglin', '24', 'balalala@ur.rochester.edu', 'valor');
INSERT INTO `user_account` VALUES ('honglin--', '2016-10-24 20:11:22.478000', '2e0212b6b6a3cc062907dae5da29ad4c', 'honglin', '25', 'nevgivin@gmail.com', 'valor');

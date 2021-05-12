-- MySQL dump 10.13  Distrib 8.0.23, for osx10.16 (x86_64)
--
-- Host: localhost    Database: cs348Project
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add guest',7,'add_guest'),(26,'Can change guest',7,'change_guest'),(27,'Can delete guest',7,'delete_guest'),(28,'Can view guest',7,'view_guest'),(29,'Can add hotel',8,'add_hotel'),(30,'Can change hotel',8,'change_hotel'),(31,'Can delete hotel',8,'delete_hotel'),(32,'Can view hotel',8,'view_hotel'),(33,'Can add reservation',9,'add_reservation'),(34,'Can change reservation',9,'change_reservation'),(35,'Can delete reservation',9,'delete_reservation'),(36,'Can view reservation',9,'view_reservation'),(37,'Can add room',10,'add_room'),(38,'Can change room',10,'change_room'),(39,'Can delete room',10,'delete_room'),(40,'Can view room',10,'view_room'),(41,'Can add feature',11,'add_feature'),(42,'Can change feature',11,'change_feature'),(43,'Can delete feature',11,'delete_feature'),(44,'Can view feature',11,'view_feature'),(45,'Can add reservation room rel',12,'add_reservationroomrel'),(46,'Can change reservation room rel',12,'change_reservationroomrel'),(47,'Can delete reservation room rel',12,'delete_reservationroomrel'),(48,'Can view reservation room rel',12,'view_reservationroomrel'),(49,'Can add feature room rel',13,'add_featureroomrel'),(50,'Can change feature room rel',13,'change_featureroomrel'),(51,'Can delete feature room rel',13,'delete_featureroomrel'),(52,'Can view feature room rel',13,'view_featureroomrel'),(53,'Can add employee',14,'add_employee'),(54,'Can change employee',14,'change_employee'),(55,'Can delete employee',14,'delete_employee'),(56,'Can view employee',14,'view_employee');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$sYgmTg9ub3IR$YyZmnOQ7r4muJlrNGz2+kkVfybUrSLUXunm7lCZxdkE=','2021-05-03 12:57:16.831723',1,'admin','','','taimoorjaved32@gmail.com',1,1,'2021-05-02 18:00:29.550859'),(13,'pbkdf2_sha256$216000$j3ARmzojiKgL$3VdUEplHneVG/YB7f/9Jb8OougT5N/EIFSXqufM06EQ=','2021-05-04 08:44:33.038700',0,'mjc123','','','mjc@yahoo.com',0,1,'2021-05-03 12:43:11.323456'),(14,'pbkdf2_sha256$216000$nkz5xFf1EVgi$6u1ATvFjV2PpjYnW7vvahMTA07brPASpE1Cp/YvF6ws=','2021-05-05 05:45:25.897317',0,'timmyX','','','taimoor.javed@hotmail.com',0,1,'2021-05-03 12:56:51.162949'),(15,'pbkdf2_sha256$216000$7NL3cYxiAlnZ$bHIZ+HPAMUWIAwHZaKe6cluCDCL1pwPsrrVzYRPV8Ps=','2021-05-04 05:10:42.484875',0,'jshaw','','','jeras@yahoo.com',0,1,'2021-05-03 15:59:29.124315'),(16,'pbkdf2_sha256$216000$xlxtaH451GD1$a2Zn+QsJzj4b4g/JVwfndpV77HZjrrrWa24mTDCe1fM=',NULL,0,'employee/emp_lang','','','emp_lang@yahoo.com',0,1,'2021-05-05 05:57:47.384960'),(17,'pbkdf2_sha256$216000$73BE7PfvhgKA$8bGKLES7EWKz3RqydyPKneJ4c3t1jC4WFrHi6CELvSY=',NULL,0,'employee/redher','','','redher@yahoo.com',0,1,'2021-05-05 05:59:42.249335'),(18,'pbkdf2_sha256$216000$hpLAtjFU3k2K$w2cutfvApL9uH5tW5iUKM1fAaHyXKk/LbCam3Kd9NVY=','2021-05-10 23:59:48.482375',0,'tjaved','','','tjaved@purdue.edu',0,1,'2021-05-06 00:21:02.169720'),(19,'pbkdf2_sha256$216000$YSHpvVFiUefY$qEwdqNFWU+R0dI+aN0KPOr9U7uHVon4SJ7WatjEm6L8=','2021-05-10 20:26:24.718297',0,'kjt3','','','kjt@yahoo.com',0,1,'2021-05-08 13:19:24.341596'),(20,'pbkdf2_sha256$216000$r4QXbYMxgMvu$N29d8vhJBJivj1U2vQfAcgroTrycSgt8E3o666l1YG4=','2021-05-10 20:26:39.817515',0,'hj5695','','','hj@yahoo.com',0,1,'2021-05-10 20:01:06.133270'),(21,'pbkdf2_sha256$216000$I2hV4ViGltUg$7sNWc9Z0baAc/seLGyOczgiORXUFqeRZac0v+tsTEXQ=','2021-05-10 20:24:03.764414',0,'employee/first1','','','first1@yahoo.com',0,1,'2021-05-10 20:23:58.603743'),(22,'pbkdf2_sha256$216000$UWM3RNI6vQqH$WY8Gq55HBrTLx/PVXTXfiAnHz3WrPpwGZMhRTUk4p/M=','2021-05-10 20:27:35.828324',0,'rguy1','','','rguy1@yahoo.com',0,1,'2021-05-10 20:27:30.162281');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-05-03 12:41:00.870447','9','abcd',3,'',4,1),(2,'2021-05-03 12:41:07.358792','4','alpha',3,'',4,1),(3,'2021-05-03 12:41:07.360748','7','alphabravo',3,'',4,1),(4,'2021-05-03 12:41:18.760288','8','dfa',3,'',4,1),(5,'2021-05-03 12:41:18.777370','5','hashim',3,'',4,1),(6,'2021-05-03 12:41:18.779047','2','javedh',3,'',4,1),(7,'2021-05-03 12:41:18.780623','3','jerome',3,'',4,1),(8,'2021-05-03 12:41:18.783039','11','kjp123',3,'',4,1),(9,'2021-05-03 12:41:18.784664','6','kjt',3,'',4,1),(10,'2021-05-03 12:41:18.786333','12','timpq',3,'',4,1),(11,'2021-05-03 12:41:18.788128','10','timtim',3,'',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(14,'guest','employee'),(11,'guest','feature'),(13,'guest','featureroomrel'),(7,'guest','guest'),(8,'guest','hotel'),(9,'guest','reservation'),(12,'guest','reservationroomrel'),(10,'guest','room'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-05-02 15:31:05.989058'),(2,'auth','0001_initial','2021-05-02 15:31:06.084719'),(3,'admin','0001_initial','2021-05-02 15:31:06.257162'),(4,'admin','0002_logentry_remove_auto_add','2021-05-02 15:31:06.323799'),(5,'admin','0003_logentry_add_action_flag_choices','2021-05-02 15:31:06.335146'),(6,'contenttypes','0002_remove_content_type_name','2021-05-02 15:31:06.399505'),(7,'auth','0002_alter_permission_name_max_length','2021-05-02 15:31:06.432630'),(8,'auth','0003_alter_user_email_max_length','2021-05-02 15:31:06.456620'),(9,'auth','0004_alter_user_username_opts','2021-05-02 15:31:06.468176'),(10,'auth','0005_alter_user_last_login_null','2021-05-02 15:31:06.500041'),(11,'auth','0006_require_contenttypes_0002','2021-05-02 15:31:06.503919'),(12,'auth','0007_alter_validators_add_error_messages','2021-05-02 15:31:06.514674'),(13,'auth','0008_alter_user_username_max_length','2021-05-02 15:31:06.552676'),(14,'auth','0009_alter_user_last_name_max_length','2021-05-02 15:31:06.593924'),(15,'auth','0010_alter_group_name_max_length','2021-05-02 15:31:06.613443'),(16,'auth','0011_update_proxy_permissions','2021-05-02 15:31:06.623215'),(17,'auth','0012_alter_user_first_name_max_length','2021-05-02 15:31:06.658232'),(18,'guest','0001_initial','2021-05-02 15:40:18.697816'),(19,'guest','0002_alter_reservationroomrel_unique_together','2021-05-02 15:40:18.714656'),(20,'guest','0003_auto_20210428_0420','2021-05-02 15:40:18.756323'),(21,'guest','0004_auto_20210428_0422','2021-05-02 15:40:18.776269'),(22,'guest','0005_alter_reservationroomrel_unique_together','2021-05-02 15:40:18.796471'),(23,'guest','0006_auto_20210428_0429','2021-05-02 15:40:18.851406'),(24,'guest','0007_delete_reservationroomrel','2021-05-02 15:40:18.860604'),(25,'guest','0008_reservationroomrel','2021-05-02 15:40:18.878663'),(26,'guest','0009_feature_featureroomrel','2021-05-02 15:40:49.239472'),(27,'guest','0010_auto_20210429_0514','2021-05-02 15:40:49.384356'),(28,'guest','0011_auto_20210429_1819','2021-05-02 15:40:49.495684'),(29,'guest','0012_featureroomrel_reservationroomrel','2021-05-02 15:40:49.525954'),(30,'sessions','0001_initial','2021-05-02 15:40:49.640425'),(31,'guest','0013_auto_20210502_0325','2021-05-03 04:58:53.365434'),(32,'guest','0014_auto_20210502_1752','2021-05-03 04:58:53.398456'),(33,'guest','0015_auto_20210503_0017','2021-05-03 16:07:01.492696'),(34,'guest','0016_alter_employee_hotel_id','2021-05-06 00:20:10.393668'),(35,'guest','0017_auto_20210505_2005','2021-05-06 00:20:11.097424'),(36,'guest','0018_employee_feature_featureroomrel_guest_hotel_reservation_reservationroomrel_room','2021-05-06 00:20:11.309227'),(37,'main_page','0004_auto_20210327_0042','2021-05-06 00:20:11.482716'),(38,'guest','0019_auto_20210510_1958','2021-05-10 19:58:44.036832');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employee_id` int NOT NULL,
  `username` varchar(50) NOT NULL,
  `hotel_id` int DEFAULT NULL,
  `first` varchar(20) NOT NULL,
  `last` varchar(20) NOT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'first1',NULL,'employee1','First');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feature_room_rel`
--

DROP TABLE IF EXISTS `feature_room_rel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feature_room_rel` (
  `id` int NOT NULL AUTO_INCREMENT,
  `feature_id` int NOT NULL,
  `room_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `feature_room_rel_feature_id_room_id_588969a2_uniq` (`feature_id`,`room_id`),
  KEY `feature_room_rel_room_id_51b6fae9_fk_room_room_id` (`room_id`),
  CONSTRAINT `feature_room_rel_feature_id_fb2fa0d5_fk_features_feature_id` FOREIGN KEY (`feature_id`) REFERENCES `features` (`feature_id`),
  CONSTRAINT `feature_room_rel_room_id_51b6fae9_fk_room_room_id` FOREIGN KEY (`room_id`) REFERENCES `room` (`room_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feature_room_rel`
--

LOCK TABLES `feature_room_rel` WRITE;
/*!40000 ALTER TABLE `feature_room_rel` DISABLE KEYS */;
/*!40000 ALTER TABLE `feature_room_rel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `features`
--

DROP TABLE IF EXISTS `features`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `features` (
  `feature_id` int NOT NULL,
  `feature` varchar(20) NOT NULL,
  `price` decimal(9,2) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`feature_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `features`
--

LOCK TABLES `features` WRITE;
/*!40000 ALTER TABLE `features` DISABLE KEYS */;
/*!40000 ALTER TABLE `features` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guest`
--

DROP TABLE IF EXISTS `guest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guest` (
  `guest_id` int NOT NULL,
  `username` varchar(50) NOT NULL,
  `first` varchar(20) NOT NULL,
  `last` varchar(20) NOT NULL,
  PRIMARY KEY (`guest_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guest`
--

LOCK TABLES `guest` WRITE;
/*!40000 ALTER TABLE `guest` DISABLE KEYS */;
INSERT INTO `guest` VALUES (1,'tjaved','Taimoor','Javed'),(2,'kjt3','Khawar','Javed'),(3,'hj5695','Hahsim','Javed'),(4,'rguy1','Random','Guys');
/*!40000 ALTER TABLE `guest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotel`
--

DROP TABLE IF EXISTS `hotel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hotel` (
  `hotel_id` int NOT NULL,
  `location` varchar(20) NOT NULL,
  `num_rooms` int NOT NULL,
  `occupancy` int NOT NULL,
  `rating` decimal(4,3) NOT NULL,
  PRIMARY KEY (`hotel_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotel`
--

LOCK TABLES `hotel` WRITE;
/*!40000 ALTER TABLE `hotel` DISABLE KEYS */;
/*!40000 ALTER TABLE `hotel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation` (
  `reservation_id` int NOT NULL,
  `check_in_date` date NOT NULL,
  `check_out_date` date NOT NULL,
  `guest_id` int NOT NULL,
  `payment_type` varchar(10) NOT NULL,
  `credit_card_number` varchar(20) DEFAULT NULL,
  `total` decimal(9,2) NOT NULL,
  PRIMARY KEY (`reservation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation`
--

LOCK TABLES `reservation` WRITE;
/*!40000 ALTER TABLE `reservation` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation_room_rel`
--

DROP TABLE IF EXISTS `reservation_room_rel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation_room_rel` (
  `id` int NOT NULL AUTO_INCREMENT,
  `reservation_id` int NOT NULL,
  `room_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reservation_room_rel_reservation_id_room_id_0983f860_uniq` (`reservation_id`,`room_id`),
  KEY `reservation_room_rel_room_id_411310c0_fk_room_room_id` (`room_id`),
  CONSTRAINT `reservation_room_rel_reservation_id_e7692a3e_fk_reservati` FOREIGN KEY (`reservation_id`) REFERENCES `reservation` (`reservation_id`),
  CONSTRAINT `reservation_room_rel_room_id_411310c0_fk_room_room_id` FOREIGN KEY (`room_id`) REFERENCES `room` (`room_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_room_rel`
--

LOCK TABLES `reservation_room_rel` WRITE;
/*!40000 ALTER TABLE `reservation_room_rel` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservation_room_rel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room` (
  `room_id` int NOT NULL,
  `hotel_id` int NOT NULL,
  `room_type` varchar(20) NOT NULL,
  `price_per_night` decimal(5,2) NOT NULL,
  `available` int NOT NULL,
  `check_in_time` time(6) NOT NULL,
  `check_out_time` time(6) NOT NULL,
  PRIMARY KEY (`room_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-10 17:26:25

CREATE DATABASE IF NOT EXISTS `dataLoader` ;

USE `dataLoader`;

CREATE TABLE IF NOT EXISTS `Communiques` (
  `id_communique` int(5) PRIMARY KEY,
  `date` varchar(50) DEFAULT "NULL",
  `nb_test` int(5) NOT NULL DEFAULT 0,
  `nb_nv_cas` int(5) NOT NULL DEFAULT 0,
  `nb_cas_contact` int(5) NOT NULL DEFAULT 0,
  `nb_cas_communautaire` int(5) NOT NULL DEFAULT 0,
  `nb_gueris` int(5) NOT NULL DEFAULT 0,
  `nb_deces` int(5) NOT NULL DEFAULT 0,
  `date_extraction`varchar(10)  DEFAULT NULL


) ;


/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acc_nm_target` (
  `value` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `cashflow__summary` AS SELECT 
 1 AS `company_name`,
 1 AS `dueDate`,
 1 AS `leftUnPaid`*/;
SET character_set_client = @saved_cs_client;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `cashflowfilter__aftertoday` AS SELECT 
 1 AS `InvoiceID`,
 1 AS `Total_invoice`,
 1 AS `tr_dt`,
 1 AS `Acc_Nm`,
 1 AS `dueDate`,
 1 AS `realDate`,
 1 AS `Paid`,
 1 AS `getpaid`,
 1 AS `total_invoice_aftertax`,
 1 AS `leftUnPaid`*/;
SET character_set_client = @saved_cs_client;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `cashflowgroup__comapnyname` AS SELECT 
 1 AS `InvoiceID`,
 1 AS `Total_invoice`,
 1 AS `tr_dt`,
 1 AS `Acc_Nm`,
 1 AS `dueDate`,
 1 AS `realDate`,
 1 AS `Paid`,
 1 AS `getpaid`,
 1 AS `total_invoice_aftertax`,
 1 AS `leftUnPaid`*/;
SET character_set_client = @saved_cs_client;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `cashflowgroupacc_nm__tr_dt` AS SELECT 
 1 AS `InvoiceID`,
 1 AS `Total_invoice`,
 1 AS `tr_dt`,
 1 AS `Acc_Nm`,
 1 AS `dueDate`,
 1 AS `realDate`,
 1 AS `Paid`,
 1 AS `getpaid`,
 1 AS `total_invoice_aftertax`,
 1 AS `leftUnPaid`*/;
SET character_set_client = @saved_cs_client;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `clints_data` AS SELECT 
 1 AS `acc_nm`,
 1 AS `tax`,
 1 AS `payment_method`*/;
SET character_set_client = @saved_cs_client;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `excel_table` (
  `tr_ty` double DEFAULT NULL,
  `Text25` double DEFAULT NULL,
  `Inv_No` double DEFAULT NULL,
  `Text91` text COLLATE utf8mb4_general_ci,
  `Acc_Nm` text COLLATE utf8mb4_general_ci,
  `sCst` double DEFAULT NULL,
  `Text103` double DEFAULT NULL,
  `Text120` bigint DEFAULT NULL,
  `Text101` double DEFAULT NULL,
  `sPrc` double DEFAULT NULL,
  `sQty` double DEFAULT NULL,
  `spkid` text COLLATE utf8mb4_general_ci,
  `tr_ds` text COLLATE utf8mb4_general_ci,
  `Itm_nm` text COLLATE utf8mb4_general_ci,
  `Itm_cd` bigint DEFAULT NULL,
  `LN_NO` bigint DEFAULT NULL,
  `TR_NO` bigint DEFAULT NULL,
  `tr_dt` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `excel_table_clients` (
  `Text25` double DEFAULT NULL,
  `rec_id` text COLLATE utf8mb4_general_ci,
  `acc_cd` double DEFAULT NULL,
  `acc_nm` text COLLATE utf8mb4_general_ci,
  `sdbt_bl` double DEFAULT NULL,
  `scrd_bl` double DEFAULT NULL,
  `Text81` text COLLATE utf8mb4_general_ci,
  `Text82` text COLLATE utf8mb4_general_ci,
  `Text83` text COLLATE utf8mb4_general_ci,
  `Text84` text COLLATE utf8mb4_general_ci,
  `Text85` double DEFAULT NULL,
  `Text86` text COLLATE utf8mb4_general_ci,
  `نص89` text COLLATE utf8mb4_general_ci,
  `نص93` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `main_sales` AS SELECT 
 1 AS `InvoiceID`,
 1 AS `Total_invoice`,
 1 AS `tr_dt`,
 1 AS `Acc_Nm`*/;
SET character_set_client = @saved_cs_client;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_sales_entry` (
  `InvoiceID` text COLLATE utf8mb4_general_ci NOT NULL,
  `dueDate` date DEFAULT NULL,
  `realDate` date DEFAULT NULL,
  `paid` tinyint(1) DEFAULT NULL,
  `getpaid` decimal(10,0) DEFAULT NULL,
  `total_invoice_aftertax` decimal(10,0) DEFAULT NULL,
  `leftunpaid` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`InvoiceID`(6))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_total_invoice_aftertax_mse` BEFORE INSERT ON `main_sales_entry` FOR EACH ROW BEGIN
    SET NEW.total_invoice_aftertax = (SELECT total_invoice FROM main_sales WHERE main_sales.InvoiceID = NEW.InvoiceID) - ((SELECT total_invoice FROM main_sales WHERE main_sales.InvoiceID = NEW.InvoiceID) * ((SELECT tax FROM clints_data WHERE clints_data.acc_nm = (SELECT Acc_nm FROM main_sales WHERE main_sales.InvoiceID = NEW.InvoiceID)) / 100));
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_leftUnPaid_before_insert_mse` BEFORE INSERT ON `main_sales_entry` FOR EACH ROW BEGIN
    SET NEW.leftUnPaid = NEW.total_invoice_aftertax - COALESCE(NEW.getpaid, 0);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `setgetpaidfrompaid_main_sales_entry` BEFORE UPDATE ON `main_sales_entry` FOR EACH ROW BEGIN
    IF NEW.paid = 1 THEN
        SET NEW.getpaid = NEW.total_invoice_aftertax;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `setrealdate_main_sales_enrty` BEFORE UPDATE ON `main_sales_entry` FOR EACH ROW BEGIN
    IF NEW.Paid THEN
        SET NEW.realDate = CURDATE();
    ELSEIF NOT NEW.Paid THEN
        SET NEW.realDate = NULL;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_leftUnPaid_before_update_mse` BEFORE UPDATE ON `main_sales_entry` FOR EACH ROW BEGIN
    SET NEW.leftUnPaid = NEW.total_invoice_aftertax - COALESCE(NEW.getpaid, 0);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `mainsales_py` AS SELECT 
 1 AS `InvoiceID`,
 1 AS `total_invoice`,
 1 AS `tr_dt`,
 1 AS `Acc_Nm`,
 1 AS `dueDate`,
 1 AS `realDate`,
 1 AS `paid`,
 1 AS `getpaid`,
 1 AS `total_invoice_aftertax`,
 1 AS `leftunpaid`*/;
SET character_set_client = @saved_cs_client;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment_due_dates` (
  `payment_method` int DEFAULT NULL,
  `due_date_expression` varchar(512) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `target_clints` (
  `name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `company_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50001 DROP VIEW IF EXISTS `cashflow__summary`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `cashflow__summary` AS select `c`.`company_name` AS `company_name`,`g`.`dueDate` AS `dueDate`,(sum((case when (`g`.`InvoiceID` like 'Ba%') then `g`.`leftunpaid` else 0 end)) - sum((case when (`g`.`InvoiceID` like 'MA%') then `g`.`leftunpaid` else 0 end))) AS `leftUnPaid` from (`mainsales_py` `g` join `target_clints` `c` on((`g`.`Acc_Nm` = `c`.`name`))) where (((`g`.`InvoiceID` like 'Ba%') or (`g`.`InvoiceID` like 'MA%')) and ((0 <> `g`.`paid`) is not true)) group by `c`.`company_name`,`g`.`dueDate` order by `g`.`dueDate` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!50001 DROP VIEW IF EXISTS `cashflowfilter__aftertoday`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `cashflowfilter__aftertoday` AS select concat('(',group_concat(distinct concat('\'',`mainsales_py`.`InvoiceID`,'\'') separator ','),',',')') AS `InvoiceID`,sum((case when (`mainsales_py`.`InvoiceID` like 'Ba%%') then `mainsales_py`.`total_invoice` else -(`mainsales_py`.`total_invoice`) end)) AS `Total_invoice`,`mainsales_py`.`tr_dt` AS `tr_dt`,`mainsales_py`.`Acc_Nm` AS `Acc_Nm`,max(`mainsales_py`.`dueDate`) AS `dueDate`,max(`mainsales_py`.`realDate`) AS `realDate`,(case when (sum(`mainsales_py`.`paid`) = count(0)) then 1 else NULL end) AS `Paid`,sum((case when (`mainsales_py`.`InvoiceID` like 'Ba%%') then `mainsales_py`.`getpaid` else -(`mainsales_py`.`getpaid`) end)) AS `getpaid`,sum((case when (`mainsales_py`.`InvoiceID` like 'Ba%%') then `mainsales_py`.`total_invoice_aftertax` else -(`mainsales_py`.`total_invoice_aftertax`) end)) AS `total_invoice_aftertax`,sum((case when (`mainsales_py`.`InvoiceID` like 'Ba%%') then `mainsales_py`.`leftunpaid` else -(`mainsales_py`.`leftunpaid`) end)) AS `leftUnPaid` from `mainsales_py` where ((`mainsales_py`.`realDate` = curdate()) or (`mainsales_py`.`realDate` is null)) group by `mainsales_py`.`InvoiceID` order by `Paid` desc,`dueDate` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!50001 DROP VIEW IF EXISTS `cashflowgroup__comapnyname`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `cashflowgroup__comapnyname` AS select concat('(',group_concat(distinct concat('\'',`mainsales_py`.`InvoiceID`,'\'') separator ','),')') AS `InvoiceID`,sum((case when (`mainsales_py`.`InvoiceID` like 'Ba%%') then `mainsales_py`.`total_invoice` else -(`mainsales_py`.`total_invoice`) end)) AS `Total_invoice`,max(`mainsales_py`.`tr_dt`) AS `tr_dt`,`target_clints`.`company_name` AS `Acc_Nm`,max(`mainsales_py`.`dueDate`) AS `dueDate`,max(`mainsales_py`.`realDate`) AS `realDate`,(case when (sum(`mainsales_py`.`paid`) = count(0)) then 1 else NULL end) AS `Paid`,sum((case when (`mainsales_py`.`InvoiceID` like 'Ba%%') then `mainsales_py`.`getpaid` else -(`mainsales_py`.`getpaid`) end)) AS `getpaid`,sum((case when (`mainsales_py`.`InvoiceID` like 'Ba%%') then `mainsales_py`.`total_invoice_aftertax` else -(`mainsales_py`.`total_invoice_aftertax`) end)) AS `total_invoice_aftertax`,sum((case when (`mainsales_py`.`InvoiceID` like 'Ba%%') then `mainsales_py`.`leftunpaid` else -(`mainsales_py`.`leftunpaid`) end)) AS `leftUnPaid` from (`mainsales_py` join `target_clints` on((`mainsales_py`.`Acc_Nm` = `target_clints`.`name`))) group by `target_clints`.`company_name`,`mainsales_py`.`dueDate` order by `Paid` desc,`dueDate` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!50001 DROP VIEW IF EXISTS `cashflowgroupacc_nm__tr_dt`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `cashflowgroupacc_nm__tr_dt` AS select concat('(',group_concat(distinct concat('\'',`mainsales_py`.`InvoiceID`,'\'') separator ','),',',')') AS `InvoiceID`,sum((case when (`mainsales_py`.`InvoiceID` like 'Ba%%') then `mainsales_py`.`total_invoice` else -(`mainsales_py`.`total_invoice`) end)) AS `Total_invoice`,`mainsales_py`.`tr_dt` AS `tr_dt`,`mainsales_py`.`Acc_Nm` AS `Acc_Nm`,max(`mainsales_py`.`dueDate`) AS `dueDate`,max(`mainsales_py`.`realDate`) AS `realDate`,(case when (sum(`mainsales_py`.`paid`) = count(0)) then 1 else NULL end) AS `Paid`,sum((case when (`mainsales_py`.`InvoiceID` like 'Ba%%') then `mainsales_py`.`getpaid` else -(`mainsales_py`.`getpaid`) end)) AS `getpaid`,sum((case when (`mainsales_py`.`InvoiceID` like 'Ba%%') then `mainsales_py`.`total_invoice_aftertax` else -(`mainsales_py`.`total_invoice_aftertax`) end)) AS `total_invoice_aftertax`,sum((case when (`mainsales_py`.`InvoiceID` like 'Ba%%') then `mainsales_py`.`leftunpaid` else -(`mainsales_py`.`leftunpaid`) end)) AS `leftUnPaid` from `mainsales_py` where ((`mainsales_py`.`realDate` > '2023-07-07') or (`mainsales_py`.`realDate` is null)) group by `mainsales_py`.`Acc_Nm`,`mainsales_py`.`tr_dt` order by `Paid` desc,`dueDate` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!50001 DROP VIEW IF EXISTS `clints_data`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `clints_data` AS with `selected_columns` as (select `excel_table_clients`.`acc_nm` AS `acc_nm`,`excel_table_clients`.`Text85` AS `Text85`,`excel_table_clients`.`نص93` AS `نص93` from `excel_table_clients`), `filtered_data` as (select `selected_columns`.`acc_nm` AS `acc_nm`,`selected_columns`.`Text85` AS `Text85`,`selected_columns`.`نص93` AS `نص93` from `selected_columns` where (`selected_columns`.`acc_nm` is not null)), `renamed_columns` as (select `filtered_data`.`acc_nm` AS `acc_nm`,`filtered_data`.`Text85` AS `tax`,`filtered_data`.`نص93` AS `payment_method` from `filtered_data`) select `renamed_columns`.`acc_nm` AS `acc_nm`,`renamed_columns`.`tax` AS `tax`,`renamed_columns`.`payment_method` AS `payment_method` from `renamed_columns` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!50001 DROP VIEW IF EXISTS `main_sales`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `main_sales` AS with `filtered` as (select `excel_table`.`tr_dt` AS `tr_dt`,`excel_table`.`TR_NO` AS `TR_NO`,`excel_table`.`tr_ds` AS `tr_ds`,`excel_table`.`Text103` AS `Text103`,`excel_table`.`Acc_Nm` AS `Acc_Nm` from `excel_table` where (((`excel_table`.`tr_ds` like '%بيع%') or (`excel_table`.`tr_ds` like '%مرتجع%')) and exists(select 1 from `acc_nm_target` where (`excel_table`.`Acc_Nm` like `acc_nm_target`.`value`)))), `renamed` as (select `filtered`.`tr_dt` AS `tr_dt`,`filtered`.`TR_NO` AS `TR_NO`,`filtered`.`tr_ds` AS `tr_ds`,`filtered`.`Text103` AS `Total_invoice`,`filtered`.`Acc_Nm` AS `Acc_Nm` from `filtered`), `formatted` as (select `renamed`.`tr_dt` AS `tr_dt`,lpad(`renamed`.`TR_NO`,4,'0') AS `TR_NO`,(case when (`renamed`.`tr_ds` = 'بيع آجل') then 'Ba' when (`renamed`.`tr_ds` = 'شراء نقدي') then 'sn' when (`renamed`.`tr_ds` = 'مرتجع آجل') then 'MA' else `renamed`.`tr_ds` end) AS `tr_ds`,`renamed`.`Total_invoice` AS `Total_invoice`,`renamed`.`Acc_Nm` AS `Acc_Nm` from `renamed`), `with_id` as (select concat(`formatted`.`tr_ds`,`formatted`.`TR_NO`) AS `InvoiceID`,`formatted`.`tr_dt` AS `tr_dt`,`formatted`.`Acc_Nm` AS `Acc_Nm`,`formatted`.`Total_invoice` AS `Total_invoice` from `formatted`) select `with_id`.`InvoiceID` AS `InvoiceID`,sum(`with_id`.`Total_invoice`) AS `Total_invoice`,max(`with_id`.`tr_dt`) AS `tr_dt`,max(`with_id`.`Acc_Nm`) AS `Acc_Nm` from `with_id` group by `with_id`.`InvoiceID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!50001 DROP VIEW IF EXISTS `mainsales_py`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `mainsales_py` AS select `ms`.`InvoiceID` AS `InvoiceID`,`ms`.`Total_invoice` AS `total_invoice`,`ms`.`tr_dt` AS `tr_dt`,`ms`.`Acc_Nm` AS `Acc_Nm`,`mse`.`dueDate` AS `dueDate`,`mse`.`realDate` AS `realDate`,`mse`.`paid` AS `paid`,`mse`.`getpaid` AS `getpaid`,`mse`.`total_invoice_aftertax` AS `total_invoice_aftertax`,`mse`.`leftunpaid` AS `leftunpaid` from (`main_sales` `ms` join `main_sales_entry` `mse` on((`ms`.`InvoiceID` = `mse`.`InvoiceID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

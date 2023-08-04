export_clints_data='select * from clints_data'
export_cashflow_gby_Acc_NmANDtr_dt=f""" SELECT * from cashflowaccnmtrdt"""
export_cashflow_fby_afterTODAY =f"""SELECT *  from cashflowFilteraftertoday"""
export_cashflow_gby_comapnyname=f"""SELECT *  from cashflowgroupcomapnyname"""
export_cashflow_report="SELECT * FROM cashflow__summary WHERE leftUnPaid <>0"
read_user_by_username="SELECT * FROM user WHERE username = %s"
callupdateCashflow_excelPRoducer='CALL update_main_sales_entry()'
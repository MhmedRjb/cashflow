export_clints_data='select * from clints_data'
export_cashflow_gby_Acc_NmANDtr_dt=f""" SELECT * from cashflowGroupAcc_Nm__tr_dt"""
export_cashflow_fby_afterTODAY =f"""SELECT *  from cashflowFilter__aftertoday"""
export_cashflow_gby_comapnyname=f"""SELECT *  from cashflowgroup__comapnyname"""
export_cashflow_report="SELECT * FROM cashflow__summary WHERE leftUnPaid <>0"
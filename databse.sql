SELECT v.tr_dt,
       v.Acc_Nm,
       v.TR_no_list,
       v.total_money,
       t.tax,
       t.paymentMethod,
       (CASE
            WHEN COALESCE(t.paymentMethod, 0) = 222 THEN DATE_ADD(LAST_DAY(v.tr_dt), INTERVAL 15 DAY)
            WHEN COALESCE(t.paymentMethod, 0) = 333 THEN
                CASE
                    WHEN DAY(v.tr_dt) <= 15 THEN DATE_ADD(DATE_ADD(v.tr_dt, INTERVAL -DAY(v.tr_dt) + 1 DAY), INTERVAL 21 DAY)
                    ELSE DATE_ADD(DATE_ADD(v.tr_dt, INTERVAL -DAY(v.tr_dt) + 1 DAY), INTERVAL 7 DAY)
                END
            WHEN COALESCE(t.paymentMethod, 0) = 0 THEN v.tr_dt
            WHEN COALESCE(t.paymentMethod, 0) = 3 THEN DATE_ADD(v.tr_dt, INTERVAL 3 DAY)
            WHEN COALESCE(t.paymentMethod, 0) = 15 THEN DATE_ADD(v.tr_dt, INTERVAL 15 DAY)
            WHEN COALESCE(t.paymentMethod, 0) = 45 THEN DATE_ADD(v.tr_dt, INTERVAL 45 DAY)
            WHEN COALESCE(t.paymentMethod, 0) = 565 THEN
                CASE
                    WHEN DAY(v.tr_dt) <= 21 THEN DATE_ADD(DATE_ADD(v.tr_dt, INTERVAL -DAY(v.tr_dt) + 1 DAY), INTERVAL 7 DAY)
                    ELSE DATE_ADD(DATE_ADD(DATE_ADD(v.tr_dt, INTERVAL -DAY(v.tr_dt) + 1 DAY), INTERVAL 1 MONTH), INTERVAL 7 DAY)
                END
        END) as payment_date
FROM (SELECT tr_dt,
             Acc_Nm,
             GROUP_CONCAT(DISTINCT TR_NO) as TR_no_list,
             SUM(CASE WHEN tr_ds = 'مرتجع آجل' THEN -Total_invoice ELSE Total_invoice END) as total_money
      FROM goods_transection
      GROUP BY tr_dt, Acc_Nm) v
JOIN clints_data t
ON v.Acc_Nm = t.acc_nm;




CREATE VIEW your_view_name1 AS
SELECT tr_dt, acc_nm, GROUP_CONCAT(DISTINCT TR_no) as TR_no_list, SUM(CASE WHEN tr_ds = 'مرتجع آجل' THEN -total_invoice ELSE total_invoice END) as total_money
FROM goods_transection
GROUP BY tr_dt, acc_nm;


CREATE VIEW your_new_view_name2 AS
SELECT v.tr_dt, v.acc_nm, v.TR_no_list, v.total_money, t.tax_percentage, t.payment_method
FROM your_view_name1 v
JOIN clints_data t
ON v.acc_nm = t.acc_num;


CREATE VIEW your_new_view_name3 AS
SELECT tr_dt,
       acc_nm,
       TR_no_list,
       total_money,
       tax_percentage,
       payment_method,
       (CASE
            WHEN payment_method IS NULL THEN tr_dt
            WHEN payment_method = 222 THEN DATE_ADD(LAST_DAY(tr_dt), INTERVAL 15 DAY)
            WHEN payment_method = 333 THEN
                CASE
                    WHEN DAY(tr_dt) <= 15 THEN DATE_ADD(DATE_ADD(tr_dt, INTERVAL -DAY(tr_dt) + 1 DAY), INTERVAL 21 DAY)
                    ELSE DATE_ADD(DATE_ADD(tr_dt, INTERVAL -DAY(tr_dt) + 1 DAY), INTERVAL 7 DAY)
                END
            WHEN payment_method = 0 THEN tr_dt
            WHEN payment_method = 3 THEN DATE_ADD(tr_dt, INTERVAL 3 DAY)
            WHEN payment_method = 15 THEN DATE_ADD(tr_dt, INTERVAL 15 DAY)
            WHEN payment_method = 45 THEN DATE_ADD(tr_dt, INTERVAL 45 DAY)
            WHEN payment_method = 565 THEN
                CASE
                    WHEN DAY(tr_dt) <= 21 THEN DATE_ADD(DATE_ADD(tr_dt, INTERVAL -DAY(tr_dt) + 1 DAY), INTERVAL 7 DAY)
                    ELSE DATE_ADD(DATE_ADD(DATE_ADD(tr_dt, INTERVAL -DAY(tr_dt) + 1 DAY), INTERVAL 1 MONTH), INTERVAL 7 DAY)
                END
        END) as payment_date
FROM your_new_view_name2;





SELECT 
    tr_dt as "تاريخ الفاتورة",
    payment_date as "تاريخ الاستحقاق",
    Acc_nm as acc_nm,
    GROUP_CONCAT(DISTINCT TR_no_list) AS "رقم الفواتير",
    SUM(total_money) AS "اجمالي المبلغ" ,
    paymentmethod as payment_method,
    CASE
        WHEN acc_nm LIKE '%مكسب%' THEN 'مكسب'
        WHEN acc_nm LIKE '%لولو%' THEN 'لولو'
        WHEN acc_nm LIKE '%خزين%' THEN 'خزين'
        WHEN acc_nm LIKE '%اليسر%' THEN 'اليسر'


        -- add more conditions here
    END AS acc_nm_group
FROM oktheone
GROUP BY tr_dt, payment_date, acc_nm_group, payment_method
HAVING acc_nm_group IS NOT NULL;

SELECT 
 tr_dt as "تاريخ الفاتورة",
 payment_date as "تاريخ الاستحقاق",
 Acc_nm as acc_nm,
 GROUP_CONCAT(DISTINCT TR_no_list) AS "رقم الفواتير",
 SUM(total_money) AS "اجمالي المبلغ" ,
 paymentmethod as payment_method,
 CASE
 WHEN acc_nm LIKE '%مكسب%' THEN 'مكسب'
 WHEN acc_nm LIKE '%لولو%' THEN 'لولو'
 WHEN acc_nm LIKE '%خزين%' THEN 'خزين'
 WHEN acc_nm LIKE '%اليسر%' THEN 'اليسر'
 ELSE acc_nm

 -- add more conditions here
 END AS acc_nm_group
FROM oktheone
GROUP BY tr_dt, payment_date, acc_nm_group, payment_method
HAVING acc_nm_group IS NOT NULL;


class DataProcessor:
    def __init__(self, file_path, expected_cols):
        self.file_path = file_path
        self.expected_cols = expected_cols

    def read_data(self):
        try:
            self.data = pd.read_excel(self.file_path)
            if not set(self.expected_cols).issubset(self.data.columns):
                raise ValueError(f'The file does not contain the expected columns: {self.expected_cols}')

     
    def creat_primary_key(self, columns, format_columns=None):
        # create a copy of the data
        data = self.data.copy()
        
        # format the specified columns
        if format_columns:
            for column, length in format_columns.items():
                data[column] = data[column].apply(lambda x: f'{x:0{length}d}')
        
        # create the primary key
        data['pk'] = data[columns].apply(lambda row: ''.join(row.values.astype(str)), axis=1)
        
        # update the data with the new primary key
        self.data = data

    def select_columns(self,wanted_cols):
        self.data = self.data[wanted_cols]

    def filter_row_null(self, column):
        self.data = self.data[self.data[column].notnull()]

    def filter_row (self, column, values):
        self.data = self.data[self.data[column].str.contains(values)]

    def clean_data(self):
        try:
            self.select_columns()
        except Exception as e:
            print(f'Error: {e}')
DELIMITER //

CREATE TRIGGER insert_new_data
AFTER INSERT ON goodstransectiontemp
FOR EACH ROW
BEGIN
    INSERT INTO yourNewTableName (dueDate, clientName, total_invoice)
    SELECT
        CASE
            WHEN payment_method IS NULL THEN NEW.tr_dt
            WHEN payment_method = 222 THEN DATE_ADD(LAST_DAY(NEW.tr_dt), INTERVAL 15 DAY)
            WHEN payment_method = 333 THEN
                CASE
                    WHEN DAY(NEW.tr_dt) <= 15 THEN DATE_ADD(DATE_ADD(NEW.tr_dt, INTERVAL -DAY(NEW.tr_dt) + 1 DAY), INTERVAL 21 DAY)
                    ELSE DATE_ADD(DATE_ADD(NEW.tr_dt, INTERVAL -DAY(NEW.tr_dt) + 1 DAY), INTERVAL 7 DAY)
                END
            WHEN payment_method = 0 THEN NEW.tr_dt
            WHEN payment_method = 3 THEN DATE_ADD(NEW.tr_dt, INTERVAL 3 DAY)
            WHEN payment_method = 15 THEN DATE_ADD(NEW.tr_dt, INTERVAL 15 DAY)
            WHEN payment_method = 45 THEN DATE_ADD(NEW.tr_dt, INTERVAL 45 DAY)
            WHEN payment_method = 565 THEN
                CASE
                    WHEN DAY(NEW.tr_dt) <= 21 THEN DATE_ADD(DATE_ADD(NEW.tr_dt, INTERVAL -DAY(NEW.tr_dt) + 1 DAY), INTERVAL 7 DAY)
                    ELSE DATE_ADD(DATE_ADD(DATE_ADD(NEW.tr_dt, INTERVAL -DAY(NEW.tr_dt) + 1 DAY), INTERVAL 1 MONTH), INTERVAL 7 DAY)
                END
        END AS dueDate,
        NEW.Acc_Nm AS clientName,
        SUM(CASE WHEN NEW.tr_ds = 'Ba' THEN NEW.Total_invoice ELSE -NEW.Total_invoice END) AS total_invoice
    FROM goodstransectiontemp t1
    JOIN clints_data t2
    ON t1.Acc_Nm = t2.acc_nm;
END//

DELIMITER ;



DELIMITER //
CREATE TRIGGER set_real_date
BEFORE INSERT ON goodstransectionte
FOR EACH ROW
BEGIN
    DECLARE payment_method INT;
    SELECT payment_method INTO payment_method FROM clints_data WHERE acc_nm = NEW.Acc_Nm;

END//
DELIMITER ;

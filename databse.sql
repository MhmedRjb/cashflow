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
             SUM(CASE WHEN tr_ds = 'return' THEN -Total_invoice ELSE Total_invoice END) as total_money
      FROM goods_transection
      GROUP BY tr_dt, Acc_Nm) v
JOIN clints_data t
ON v.Acc_Nm = t.acc_nm;

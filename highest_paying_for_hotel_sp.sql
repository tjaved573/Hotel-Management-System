DROP PROCEDURE IF EXISTS PayingCustomers;

DELIMITER //

CREATE PROCEDURE PayingCustomers ( IN h_id int )

BEGIN
    DECLARE done int default 0;
    DECLARE curr_guest_id int;
    DECLARE curr_total DECIMAL(9,2);
    DECLARE curr_first VARCHAR(20);
    DECLARE curr_last VARCHAR(20);
    DECLARE cur CURSOR FOR
        SELECT guest_id, sum(total) as sum_total
        FROM reservation
        NATURAL JOIN reservation_room_rel
        NATURAL JOIN room
        WHERE hotel_id = h_id
        GROUP BY guest_id
        ORDER BY sum_total DESC;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    DROP TABLE IF EXISTS temp_table;
    CREATE TABLE temp_table(first_name VARCHAR(20), last_name VARCHAR(20), total DECIMAL(9,2));
    OPEN cur;
    ITR:LOOP
        FETCH cur into curr_guest_id, curr_total;
        IF done = 1 THEN
            CLOSE cur;
            LEAVE ITR;
        END IF;

        SELECT first, last INTO curr_first, curr_last
        FROM guest
        WHERE guest_id = curr_guest_id;

        INSERT INTO temp_table VALUES (curr_first, curr_last, curr_total);
    END LOOP;

    SELECT * FROM temp_table;
    DROP TABLE temp_table;

END //
DELIMITER ;
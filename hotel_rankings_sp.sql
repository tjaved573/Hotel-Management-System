DROP PROCEDURE IF EXISTS RankHotels;

DELIMITER //

CREATE PROCEDURE RankHotels ( )

BEGIN
    DECLARE done int default 0;
    DECLARE company_total DECIMAL(12,2);
    DECLARE curr_hotel_id int;
    DECLARE curr_total DECIMAL(9,2);
    DECLARE curr_location VARCHAR(20);
    DECLARE curr_percent DECIMAL(5,4);
    DECLARE cur CURSOR FOR
        SELECT hotel_id, sum(total) as sum_total
        FROM reservation
        NATURAL JOIN reservation_room_rel
        NATURAL JOIN room
        GROUP BY hotel_id
        ORDER BY sum_total DESC;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    SELECT sum(total) INTO company_total
    FROM reservation;
    DROP TABLE IF EXISTS temp_table;
    CREATE TABLE temp_table(location VARCHAR(20), percent DECIMAL(5,4));
    OPEN cur;
    ITR:LOOP
        FETCH cur into curr_hotel_id, curr_total;
        IF done = 1 THEN
            CLOSE cur;
            LEAVE ITR;
        END IF;

        SELECT location INTO curr_location
        FROM hotel
        WHERE hotel_id = curr_hotel_id;

        SET curr_percent = curr_total / company_total;

        INSERT INTO temp_table VALUES (curr_location, curr_percent);
    END LOOP;

    SELECT * FROM temp_table;
    DROP TABLE temp_table;

END //
DELIMITER ;
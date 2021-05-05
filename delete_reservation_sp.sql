DROP PROCEDURE IF EXISTS DeleteReservation;

DELIMITER //

CREATE PROCEDURE DeleteReservation ( IN del_res_id int )

BEGIN
    
    DECLARE done int default 0;
    DECLARE curr_id int;
    DECLARE cur CURSOR FOR SELECT room_id FROM reservation_room_rel WHERE reservation_id = del_res_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;
    ITR:LOOP
        FETCH cur into curr_id;
        IF done = 1 THEN
            CLOSE cur;
            LEAVE ITR;
        END IF;
        UPDATE room SET available=1 WHERE room_id = curr_id;
    END LOOP;
    DELETE FROM reservation_room_rel WHERE reservation_id = del_res_id;
    DELETE FROM reservation WHERE reservation_id = del_res_id;
    

END //
DELIMITER ;
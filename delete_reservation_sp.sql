DROP PROCEDURE IF EXISTS DeleteReservation;

DELIMITER //

CREATE PROCEDURE DeleteReservation ( IN del_res_id int )

BEGIN
    
    DELETE FROM reservation_room_rel WHERE reservation_id = del_res_id;
    DELETE FROM reservation WHERE reservation_id = del_res_id;

END //
DELIMITER ;
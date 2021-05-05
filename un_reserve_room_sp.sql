DROP PROCEDURE IF EXISTS unReserveRoom;

DELIMITER //
CREATE PROCEDURE unReserveRoom (
    r_id INT
)
BEGIN
    UPDATE room 
        SET available=0
        WHERE room_id = r_id;
END //
DELIMITER ;
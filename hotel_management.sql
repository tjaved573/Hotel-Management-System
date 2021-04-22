SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS hotel;
DROP TABLE IF EXISTS room;
DROP TABLE IF EXISTS guest;
DROP TABLE IF EXISTS reservation;
DROP TABLE IF EXISTS features;
DROP TABLE IF EXISTS feature_room_rel;
DROP TABLE IF EXISTS reservation_room_rel;

-- Data should be present here on start up
CREATE TABLE hotel (
    hotel_id integer NOT NULL,
    location varchar(20),
    num_rooms integer,
    occupancy integer,
    rating decimal(4,3),
    PRIMARY KEY (hotel_id)
);

-- Data should be present here on start up
CREATE TABLE room (
    room_id integer NOT NULL,
    hotel_id integer,
    room_type varchar(20),
    price_per_night decimal(5,2),
    available tinyint(4),
    check_in_time time, 
    check_out_time time,
    PRIMARY KEY (room_id)
);

CREATE TABLE guest (
    guest_id integer NOT NULL,
    first varchar(20),
    last varchar(20),
    PRIMARY KEY (guest_id)
);

CREATE TABLE employee (
    employee_id integer NOT NULL,
    hotel_id integer,
    first varchar(20),
    last varchar(20),
    PRIMARY KEY (employee_id)
);

CREATE TABLE reservation (
    reservation_id integer NOT NULL,
    check_in_date date,
    check_out_date date,
    guest_id integer,
    payment_type varchar(10),
    credit_card_number varchar(20),
    total decimal(9,2),
    PRIMARY KEY (reservation_id)
);

-- Data should be present here on start up
CREATE TABLE features (
    feature_id integer NOT NULL,
    feature varchar(20),
    price decimal(9,2),
    description varchar(255),
    PRIMARY KEY (feature_id)
);

-- Data should be present here on start up
CREATE TABLE feature_room_rel (
    feature_id integer NOT NULL,
    room_id integer NOT NULL,
    PRIMARY KEY (feature_id, room_id)
);

CREATE TABLE reservation_room_rel (
    reservation_id integer NOT NULL,
    room_id integer NOT NULL,
    PRIMARY KEY (reservation_id, room_id)
);

SET FOREIGN_KEY_CHECKS=1;

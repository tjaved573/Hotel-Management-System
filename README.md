# CS348Project
CS348-Project-Hotel Management <br />

To run the app: <br />
python manage.py runserver <br />

DB instance on GCP: HotelManagementSystem-CS348 <br />
DB name on GCP: datacs348project <br />


## SQL Queries:

Django is based around ORM - so around 70% of our queries interact with MySQl
in this way.


## Indexes:<br />

create index res_room_rel_idx on reservation (reservation_id); <br />
create index room_av_idx on room (available); <br />
create index room_price_idx on room (price_per_night); <br />
create index res_guest_idx on reservation (guest_id); <br />

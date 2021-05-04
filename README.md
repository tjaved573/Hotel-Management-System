# CS348Project
CS348-Project-Hotel Management <br />

To run the app: <br />
python manage.py runserver <br />

DB instance on GCP: HotelManagementSystem-CS348 <br />
DB name on GCP: datacs348project <br />


Indexes:<br />

create index room_index on room (price_per_night); <br />
create index room_av_index on room (available); <br />
create index av_rating on hotel (rating);<br />
create index hotel_occupancy on hotel (occupancy);<br />

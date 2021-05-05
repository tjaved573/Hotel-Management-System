# CS348Project
CS348-Project-Hotel Management <br />

To run the app: <br />
python manage.py runserver <br />

DB instance on GCP: HotelManagementSystem-CS348 <br />
DB name on GCP: datacs348project <br />


## SQL Queries:

Django is based around ORM - so around 70% of our queries interact with MySQl
in this way. Any time you see something like `ModelName.objects.get()` or `ModelName.objects.all()`
in one of our `views.py` files, this is running a `SELECT` query. When you have one of these lines
followed by `.filter(some filter here)` or `.get(some filter here)`, this is equivalent to having a `WHERE` clause.
For more complicated ORM queries, we save results to local variables and manually processes them in Python.<br />
Formal raw SQL aggregate and group-by queries are used for generating reports in our `employee` app (in the form of stored procedures), please see `highest_paying_for_hotel_sp.sql` and `hotel_rankings_sp.sql` for these queries.<br />

## Indexes:<br />

create index res_room_rel_idx on reservation (reservation_id); <br />
create index room_av_idx on room (available); <br />
create index room_price_idx on room (price_per_night); <br />
create index res_guest_idx on reservation (guest_id); <br />

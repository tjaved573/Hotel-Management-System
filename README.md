# CS348Project
CS348-Project-Hotel Management <br />

To run the app: <br />

Clone git repository<br />
Download all libraries found in `requirements.txt` (also you need Python 3.7 or greater).<br />
Load dummy data of your choosing into the tables: `hotel`, `room`, `features`, and `feature_room_rel`.
To see examples of this data, please look in `data/`.<br />
You may need to then run: `python manage.py makemigrations` followed by `python manage.py migrate`.<br />
python manage.py runserver <br />


## SQL Queries:

Django is based around ORM - so approximately 60% of our queries interact with MySQl
in this way. Any time you see something like `ModelName.objects.get()` or `ModelName.objects.all()`
in one of our `views.py` files, this is running a `SELECT` query. When you have one of these lines
followed by `.filter(some filter here)` or `.get(some filter here)`, this is equivalent to having a `WHERE` clause. 
For more complicated ORM queries, we save results to local variables and manually processes them in Python.<br />
Formal raw SQL aggregate and group-by queries are used for generating reports in our `employee` app (in the form of stored procedures), please see `highest_paying_for_hotel_sp.sql` and `hotel_rankings_sp.sql` for these queries.<br />

## Notes on ORM:

As mentioned, Django is very supportive of ORM. After settuping up our local databases and connecting 
this with our Django project, we created class representations of our tables in `guest/models.py`.

## Notes on Stored Procedures:

Stored procedures are used to retrieve information for employee reports as well as maintain accurate 
relationships between entities. For the employee table, the stored procedures found in `highest_paying_for_hotel_sp.sql` and `hotel_rankings_sp.sql` are called. These two stored both use different aggregate select statements, multiple joins, as well as they iterate over a cursor. In addition to these, `guest/views.py` calls a stored procedure found in `delete_reservation_sp.sql` whenever a guest deletes the record of one of their reservations. In that particular case, the stored procedure iteratues over a cursor and sets the availability of each room for the reservation back to 1 before deleting the reservation from the `reservation_room_rel` table and then the `reservation` table. Finally, the `unReserverRoom` stored procedure found in `un_reserve_room_sp.sql` simply sets the availability of a room to 0 whenever a guest has made a reservation.

## Transactions and Isolation Levels:

Transactions are used in three major places in this project. The first is when a guest is making a reservation. This transaction starts immediately after the guest has clicked the final button in the form to make the reservation. This transaction is set with an isolation level of repeatable read because multiple guests might attempt to reserve the same room at the same time. If this were the case, bits of each transaction may both check and confirm the room is available at the same time before only one can reserve the room. We don't need a more restrictive isolation level in this case, there is no possibility of phantom data.<br/>
The other two transactions are placed around the stored procedures for the employee reports. These two transactions only require isolation levels of read uncommitted, since we are only getting approximate data that doesn't entirely matter for the functionality of our application.

## Indexes:<br />

create index res_room_rel_idx on reservation (reservation_id); <br />
create index room_av_idx on room (available); <br />
create index room_price_idx on room (price_per_night); <br />
create index res_guest_idx on reservation (guest_id); <br />

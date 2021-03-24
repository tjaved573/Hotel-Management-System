import pandas as pd
import names
import datetime
import random


# Parameters
SINGLE_FREQ=0.2
DOUBLE_FREQ=0.6
SUITE_FREQ=0.2
SINGLE_PRICE=130.0
DOUBLE_PRICE=160.0
SUITE_PRICE=200.0
NORMAL_CHECK_IN="14:00:00"      # Normal rooms have to check in after 2 PM
NORMAL_CHECK_OUT="11:00:00"     # Normal rooms have to check out by 11 AM
SUITE_CHECK_IN="11:00:00"       # Suites can check in as early as 11 AM
SUITE_CHECK_OUT="17:00:00"      # Suites can check out by 5 PM
ROOM_TYPES_AND_INFO={
    "single":[SINGLE_FREQ, SINGLE_PRICE, NORMAL_CHECK_IN, NORMAL_CHECK_OUT, {"jacuzzi":0.0,"minibar":0.1,"balcony":0.5,"kitchen":0.25}],
    "double":[DOUBLE_FREQ, DOUBLE_PRICE, NORMAL_CHECK_IN, NORMAL_CHECK_OUT, {"jacuzzi":0.0,"minibar":0.25,"balcony":0.5,"kitchen":0.25}],
    "suite":[SUITE_FREQ, SUITE_PRICE, SUITE_CHECK_IN, SUITE_CHECK_OUT, {"jacuzzi":1.0,"minibar":1.0,"balcony":1.0,"kitchen":0.5}]
}
CITIES_AND_MARKUP=dict.fromkeys(["Manchester", "Nampa", "Beaumont", "Grand Prairie", "Laredo", "Shreveport", "Philadelphia", "Gresham", "Folsom", "Kansas City"])
PAYMENT_TYPES=["cash", "credit"]
ROOM_RANGE=(10,20)          # Hotels can have between 10 and 20 rooms
OCCUPANCY_RANGE=(20,100)    # To be divided by 100 to get percent
RATING_RANGE=(0,500)        # To be devided by 100
STAY_RANGE=(1,14)           # Guests stay between 1 and 14 days
MARKUP_RANGE=(-20,20)
NUM_HOTELS=3
NUM_GUESTS=10
TODAYS_DATE=datetime.datetime.today()


def save_to_csv(data, filename):
    df = pd.DataFrame(data=data)
    df.to_csv(filename, header=False, index=False)


hotel = pd.DataFrame(columns=["hotel_id", "location", "num_rooms", "occupancy", "rating"])
room = pd.DataFrame(columns=["room_id", "hotel_id", "room_type", "price_per_night", "available", "check_in_time", "check_out_time"])
guest = pd.DataFrame(columns=["guest_id", "first", "last"])

reservation = pd.DataFrame(columns=["reservation_id", "check_in_date", "check_out_date", "guest_id", "payment_type", "credit_card_number", "total"])

feature_room_rel = pd.DataFrame(columns=["feature_id", "room_id"])
reservation_room_rel = pd.DataFrame(columns=["reservation_id", "room_id"])

features = {
    "feature_id":[1,2,3,4],
    "feature":["jacuzzi","minibar","balcony","kitchen"],
    "price":[50,75,25,85],
    "description":["includes a built-in jacuzzi","includes a minibar","includes a balcony","includes a kitchen"]
}
features = pd.DataFrame.from_dict(features)


# Generate hotel data
for hotel_idx in range(NUM_HOTELS):
    hotel_id = hotel_idx+1
    location = random.choice([loc for loc in CITIES_AND_MARKUP.keys() if loc not in list(hotel["location"])])
    num_rooms = random.randint(*ROOM_RANGE)
    occupancy = int(num_rooms * random.randint(*OCCUPANCY_RANGE)/100)
    rating = random.randint(*RATING_RANGE) / 100
    hotel.loc[hotel_idx]=[hotel_id, location, num_rooms, occupancy, rating]

    CITIES_AND_MARKUP[location] = random.randint(*MARKUP_RANGE)    # Choosing hotel markup

    # Generate room data, for each hotel
    for room_idx in range(num_rooms):
        room_id = len(room.index)
        room_type = random.choices(list(ROOM_TYPES_AND_INFO.keys()), [e[0] for e in ROOM_TYPES_AND_INFO.values()])[0]
        price_per_night = ROOM_TYPES_AND_INFO[room_type][1] + CITIES_AND_MARKUP[location]
        available=1     # This attribute updated while generating reservation data
        check_in_time = ROOM_TYPES_AND_INFO[room_type][2]
        check_out_time = ROOM_TYPES_AND_INFO[room_type][3]
        room.loc[room_id]=[room_id+1, hotel_id, room_type, price_per_night, available, check_in_time, check_out_time]


# Build feature_room_rel table
for idx, r in room.iterrows():
    for f_idx, f in enumerate(features["feature"]):
        if random.uniform(0.0,1.0) <= ROOM_TYPES_AND_INFO[r["room_type"]][4][f]:
            feature_id = len(feature_room_rel.index)
            feature_room_rel.loc[feature_id]=[features["feature_id"][f_idx], r["room_id"]]


# Generate guest data
for guest_idx in range(NUM_GUESTS):
    guest_id = guest_idx+1
    first = names.get_first_name()
    last = names.get_last_name()
    guest.loc[guest_idx]=[guest_id, first, last]

    num_reservations=random.randint(1,6)

    # Generate reservation data, for each guest
    for res_idx in range(num_reservations):
        dur = random.randint(*STAY_RANGE)
        days_in_past = random.randint(0,365)
        check_in_date = TODAYS_DATE - datetime.timedelta(days=days_in_past)
        check_out_date = check_in_date + datetime.timedelta(days=dur)

        reservation_id = len(reservation.index)
        total = 0

        num_rooms = random.randint(1,3)
        rand_hotel = random.choice(list(hotel["hotel_id"]))
        rooms = random.sample(list(room.loc[room.hotel_id==rand_hotel]["room_id"]),k=num_rooms)
        for room_id in rooms:
            # TODO: Figure out if room_id is currently reserved during the span
            if check_out_date >= TODAYS_DATE:
                print(f"{check_out_date} is later than {TODAYS_DATE}. Reservation {reservation_id+1}, room {room_id}")
                room.loc[room["room_id"]==room_id, "available"] = 0

            reservation_room_rel_id = len(reservation_room_rel.index)
            reservation_room_rel.loc[reservation_room_rel_id]=[reservation_id+1, room_id]
            total += float(room.loc[room.room_id==room_id, "price_per_night"]) * dur
            room_features = list(feature_room_rel.loc[feature_room_rel.room_id==room_id]["feature_id"])
            for f in room_features:
                total += float(features.loc[features.feature_id==f, "price"]) * dur

        payment_type = random.choices(["cash", "credit"], [0.1, 0.9])[0]
        credit_card_number = "".join([str(random.randint(0,9)) for i in range(16)]) if payment_type=="credit" else "Null"

        reservation.loc[reservation_id]=[reservation_id+1, check_in_date.strftime("%Y-%m-%d"), check_out_date.strftime("%Y-%m-%d"), guest_id, payment_type, credit_card_number, total]


save_to_csv(hotel, "data/hotel.csv")
save_to_csv(room, "data/room.csv")
save_to_csv(guest, "data/guest.csv")
save_to_csv(reservation, "data/reservation.csv")
save_to_csv(feature_room_rel, "data/feature_room_rel.csv")
save_to_csv(reservation_room_rel, "data/reservation_room_rel.csv")
save_to_csv(features, "data/features.csv")


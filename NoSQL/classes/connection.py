import pymongo
import kayak_scrapper
from pymongo import MongoClient

my_client = MongoClient("mongodb://localhost:27017/")
mydb = my_client["my_database"]
mycol = mydb["customers"]

list_of_flights = []


def saveAll():
    try:
        flights_list = kayak_scrapper.kayak_scrapper(
            "https://www.kayak.com/flights/AMS-IKA/2022-02-02?sort=bestflight_a",
            "2/2/2022", "Amsterdam", "Tehran")
        # flights_list.append(kayak_scrapper.kayak_scrapper(
        #     "https://www.kayak.com/flights/IKA-IST/2022-02-03?sort=bestflight_a",
        #     "3/2/2022", "Tehran", "Istanbul"))
        # flights_list.append(kayak_scrapper.kayak_scrapper(
        #     "https://www.kayak.com/flights/IST-IKA/2022-02-03?sort=bestflight_a",
        #     "3/2/2022", "Istanbul", "Tehran"))
        # flights_list.append(kayak_scrapper.kayak_scrapper(
        #     "https://www.kayak.com/flights/DXB-IKA/2022-02-04?sort=bestflight_a",
        #     "4/2/2022", "Dubai", "Tehran"))
        # flights_list.append(kayak_scrapper.kayak_scrapper(
        #     "https://www.kayak.com/flights/IKA-DXB/2022-02-04?sort=bestflight_a",
        #     "4/2/2022", "Tehran", "Dubai"))
        for f in flights_list:
            list_of_flights.append(vars(f))

        x = mycol.insert_many(list_of_flights)
        # print(x.inserted_ids)
    except Exception:
        try:
            saveAll()
        except Exception:
            saveAll()


# query
# 1
def first(dateEntered):
    result1 = mycol.find({"date": dateEntered})
    return result1


# 2
def second(minCost, maxCost):
    result2 = mycol.find(({
        "price": {"$in": [minCost, maxCost]}}))
    return result2


# 3
def third(dep, des):
    result3 = mycol.aggregate({ "$group:": [
        {
        "beginning": dep,
        "destination": des
        },
        {
        "max": { "$max": "$price"},
        "min": { "$min": "$price"}
        }
    ]})
    return result3


# 4
def forth(dep, des):
    result = mycol.aggregate({"$group": {
        {
            "beginning": dep,
            "destination": des
        },
        {
            "pop": {"$avg": "$price"},  # average price
            "sum": {"$sum": "$price"}  # sum of prices
        }
    }})
    return result


# 5
def fifth(type):
    return mycol.aggregate({"$group": {
        {
            "flight_class": type
        },
        {
            "max": {"$max": "$price"},
            "min": {"$min": "$price"},
            "pop": {"$avg": "$price"},  # average price
            "sum": {"$sum": "$price"}  # sum of prices
        }
    }})


# 6
def sixth(dep, des, minCost, maxCost):
    return mycol.aggregate({"$group": {
        {
            "beginning": dep,
            "destination": des,
            "price": {"$in": [minCost, maxCost]}
        },
        {
            "min": {"$min": "$price"}
        }
    }})


# 7
def seventh(dep, des, capacity):
    return mycol.find({"$group": {
        "beginning": dep,
        "destination": des,
        "capacity": capacity
    }})


# 8
def eagth(dep, des, minCost, maxCost, capacity):
    return mycol.aggregate({"$group": {
        {
            "beginning": dep,
            "destination": des,
            "capacity": capacity,
            "price": {"$in": [minCost, maxCost]}
        },
        {
            "min": {"$min": "$price"}
        }
    }})


# 9
def ninth(dep, des, dateEntered):
    return mycol.aggregate({"$group": {
        {
            "beginning": dep,
            "destination": des,
            "date": dateEntered
        },
        {
            "airline": 1
        }
    }})


# 10
def tenth(airline, dateEntered):
    return mycol.delete_many({"$group": {
        "airline": airline,
        "date": dateEntered
    }})


# 11
def eleventh(capacity, new_capacity):
    return mycol.find_one_and_update({"capacity": capacity}, {"capacity": new_capacity})


# 12
def twelveth(dep, des, dateEntered, capacity, new_capacity):
    return mycol.update_many({
        "beginning": dep,
        "destination": des,
        "date": dateEntered,
        "capacity": capacity
    },
        {
            "$set": {"capacity": new_capacity}
        }
    )


# 13
def theerteenth(dep, des, dateEntered):
    result13 = mycol.aggregate({"$group": {
        {
            "beginning": dep,
            "destination": des,
            "date": dateEntered
        },
        {
            "beginning_airport": 1, "destination_airport": 1
        }
    }})
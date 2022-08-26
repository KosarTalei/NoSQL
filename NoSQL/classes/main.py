from json import dumps

import connection


def main():

    # crawling webpage and save data
    connection.saveAll()

    while True:
        try:
            result = ""
            number = int(input("number of query:"))
            if number == 1:
                date_entered = input("Enter the date time: d/m/y")
                result = connection.first(date_entered)

            elif number == 2:
                min_cost = input("Enter the min cost: ")
                max_cost = input("Enter the max cost: ")
                result = connection.second(min_cost, max_cost)

            elif number == 3:
                dep = input("Enter the beginning: ")
                des = input("Enter the destination : ")
                result = connection.third(dep, des)

            elif number == 4:
                dep = input("Enter the beginning: ")
                des = input("Enter the destination : ")
                result = connection.forth(dep, des)

            elif number == 5:
                flight_class = input("Enter the flight class : ")
                result = connection.fifth(flight_class)

            elif number == 6:
                dep = input("Enter the beginning: ")
                des = input("Enter the destination : ")
                min_cost = input("Enter the min cost: ")
                max_cost = input("Enter the max cost: ")
                result = connection.sixth(dep, des, min_cost, max_cost
                                          )
            elif number == 7:
                dep = input("Enter the beginning: ")
                des = input("Enter the destination : ")
                cap = input("Enter the flight capacity : ")
                result = connection.seventh(dep, des, cap)

            elif number == 8:
                dep = input("Enter the beginning: ")
                des = input("Enter the destination : ")
                min_cost = input("Enter the min cost: ")
                max_cost = input("Enter the max cost: ")
                result = connection.eagth(dep, des, min_cost, max_cost)

            elif number == 9:
                dep = input("Enter the beginning: ")
                des = input("Enter the destination : ")
                date_entered = input("Enter the date time: d/m/y")
                result = connection.ninth(dep, des, date_entered)

            elif number == 10:
                airline = input("Enter airline name: ")
                date_entered = input("Enter the date time: d/m/y")
                result = connection.tenth(airline, date_entered)

            elif number == 11:
                cap = input("Enter flight capacity number: ")
                new = input("Enter new capacity number: ")
                result = connection.eleventh(cap, new)

            elif number == 12:
                dep = input("Enter the beginning: ")
                des = input("Enter the destination : ")
                date_entered = input("Enter the date time: d/m/y")
                cap = input("Enter flight capacity number: ")
                new = input("Enter new capacity number: ")
                result = connection.twelveth(dep, des, date_entered, cap, new)

            elif number == 13:
                dep = input("Enter the beginning: ")
                des = input("Enter the destination : ")
                date_entered = input("Enter the date time: d/m/y")
                result = connection.theerteenth(dep, des, date_entered)

            for dic in result:
                print(dic)

        except Exception:
            continue

        print("***************************")
        x = input("Enter 0 to stop the program or any other keys to continue")
        print("***************************")
        if x == 0:
            break


if __name__ == '__main__':
    main()
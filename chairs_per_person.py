try:
    f = open("reservations.csv")
except FileNotFoundError:
    print("File must be of type .csv (comma separated values)")
    f = open("reservations")

for reservation in f:
    name, number = reservation.split(",")
    try:
        chairs_per_person = 50 / int(number)
    except ValueError:
        print("Value must be numerical of integral type")
    except ZeroDivisionError:
        print("A booking cannot contain a value of 0 people")
    print("{} will get {} chairs per person".format(name, chairs_per_person))

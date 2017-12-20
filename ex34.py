import json
from pprint import pprint

name = raw_input("get name:")
birthdays = json.load(open("birthdaysJson.txt"))
birthdaysDic = birthdays["birthday"]

for b in birthdaysDic:
    try:
        date = b[name]
        print "the date is: " + date
    except:
        pass
t = 1

def getBrithdayAsDic(fileName):
    d = {}
    with open(fileName) as f:
        for line in f:
            (key, val) = line.split()
            d[key] = val
    return d


birthdaysDic = getBrithdayAsDic("birthdays.txt")
print "Welcome to the birthday dictionary. We know the birthdays of:"
for b in birthdaysDic.keys():
    print b

name = raw_input("Who's birthday do you want to look up?")
print name + "'s birthday is " + birthdaysDic.get(name)
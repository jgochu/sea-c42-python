# 'hw4 - 3 simple functions with NameError, TypeError, AttributeError.'


def exhibit_name_error():
    if andrew > 5:
        print ("Hello you.")
    else:
        print ("Your number is too low.")


def exhibit_attribute_error():
    x = 1
    x.sort()


def exhibit_type_error():
    x = "5"
    print (x + 1)

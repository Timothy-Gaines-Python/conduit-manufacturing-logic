# Working the saw
def metering(footage, good_condition):
    if footage == 25 and good_condition == True:
        print("CUT, TRIM, AND TAPE")
    elif footage == 25 and good_condition == False:
        print("Strip!")
    elif footage < 25:
        print("Strip!")
    else:
        print("Wait For Conduit")


# boxing the Conduit
def boxing(good_condition):
    if good_condition == True:
        print("BOX, STACK AND Label")
    else:
        print("Wait For Conduit")



# Calling all functions

metering(25, True)
boxing(True)

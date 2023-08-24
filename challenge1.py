#input hours, min(range(59)), am/pm 
#convert the pm to 24 by adding 12 to the hours
#the am should be converted to a 4 digit time
#all time must be in 00:00pm formart
#index 0 and 1 to be added
#index -1 and -2 to be checked if they equals am or pm
#if "pm" add 12 to index[:2] to convert the hours to 24 hrs with thier types as int
#return the sum of the above statement and index[3:5]
# if index[-2:] == "am index[:2]" and return 00 and add index[3:5] as a string


def clock(saa):
    if int(saa[3:5]) <60 and int(saa[:2]) < 13:

        if saa[-2:] =="pm" and saa[:2] !="12":
            conv= int(saa[:2]) + 12
            time=str(conv) + saa[3:5] + "hrs"
            print(saa)
            print(time)

        elif saa[-2:] =="pm" and saa[:2] == "12":
            time2="00" +saa[3:5] + "hrs"
            print(saa)
            print(time2)

        if saa[-2:] == "am":
            time3=str(saa[:2]) + saa[3:5] + "hrs"
            print(time3)
    else:
        print("The minutes you put are invalid")
    if int(saa[:2]) > 12:
        print("The hours you put are not valid.")

    #     print(saa)
clock("06:45pm")
clock("13:76pm")
clock("12:09pm")
clock("01:45am")
clock("12:12am")
clock("02:87pm")
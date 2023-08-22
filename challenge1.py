#input hours, min(range(59)), am/pm
#convert the pm to 24 by adding 12 to the hours
#the am should be converted to a 4 digit time


def clock(time):
    for t in time:
        range(0,12)
    if time[-1]=="pm":
        conv = time[0] + 12
        print(conv)

clock("9:34" pm)
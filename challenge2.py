def numbre(a,b,c):
    uno= a *-1
    dos=b * -1
    tres=c * -1
    if (uno ==(-a)) and ((dos ==(-b)) or (tres == (-c))):
        print("uno",uno, "dos",dos, "tres",tres)
        print("true")
    elif (dos == -b) and ((uno == -a) or (tres ==-c)):
        print("uno",uno, "dos",dos, "tres",tres)
        print("True2")
    elif (tres == -c) and ((dos == -b) or (uno ==-a)):
        print("uno",uno, "dos",dos, "tres",tres)
        print("True3")
    else:
        print("False")
numbre(-2,3,4)

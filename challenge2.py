# def numbre(a,b,c):
#     uno= -a
#     dos=-b 
#     tres=-c
#     if uno ==(-a) and ((dos ==-b) or (tres ==-c)):
#         print("uno",uno, "dos",dos, "tres",tres)
#         return print("True")
#     if (dos == -b) and ((uno == -a) or (tres ==-c)):
#         print("uno",uno, "dos",dos, "tres",tres)
#         return print("True2")
#     if (tres == -c) and (dos == -b) or (uno ==-a):
#         print("uno",uno, "dos",dos, "tres",tres)
#         return print("True3") 
#     else:
#         print("False")
# numbre(2,3,-6)


# def numbre(a, b, c):
#     uno = (a*-1)
#     dos = (b*-1)
#     tres = (c*-1)
#     print(uno, dos, tres)
#     print(a,b,c)
#     print((a*-1), (b*-1), (c*-1))
#     if uno == (a*-1) and ((dos == (b*-1)) or (tres == (c*-1))):
#         print("Conditions met for case 1")
#         return True
    
#     # if (dos == -b) and ((uno == -a) or (tres == -c)):
#     #     print("Conditions met for case 2")
#     #     return True
    
#     # if (tres == -c) and ((dos == -b) or (uno == -a)):
#     #     print("Conditions met for case 3")
#     #     return True

    
#     # print("Conditions not met for any case")
#     # return False

# numbre(-2, 3, -6)


# def numbre(a, b, c):
#     uno = -a
#     dos = -b
#     tres = -c
    
#     if (uno == -a) and (((dos == -b) or (tres == -c))):
#         print("Conditions met for case 1")
#         return True
    
#     if (dos == -b) and (((uno == -a) or (tres == -c))):
#         print("Conditions met for case 2")
#         return True
    
#     if (tres == -c) and ((dos == -b) or (uno == -a)):
#         print("Conditions met for case 3")
#         return True
    
#     print("Conditions not met for any case")
#     return False

# numbre(2, 3, -6)


def numbre(a,b,c):
    count=0 
    if a > 0:
        count+=1
    if b > 0:
        count+=1
    if c > 0:
        count +=1
    else:
        print("Neither 2 numbers are positive")
    return count == 2
print(numbre (4,7,-9))

print(numbre (-2,7,-9))
print(numbre (4,-10,-9))
print(numbre (99,12,67))
print(numbre (-44,23,11))

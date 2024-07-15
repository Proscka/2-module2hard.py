import random
def stonec():
    num=random.randit=(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
    win = random. choice(num)
    return win
win=stonec()
print(win)
num=(20)
str_=""
for i in range(1, num + 1):

    for j in range(1, num + 1):

            if i != j and num % (i + j) == 0 and i<j:
                str_ += (str(i) + (str(j)))
                print(str_)















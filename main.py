#Activity1
def numberofbits(n):
    zeroes=0
    ones=0
    while (n) :
        if (n&1==1):
            ones+=1
        else:
            zeroes+=1
        n>>=1
    print("Number of ones: ",ones,"Number of zeroes: ",zeroes)
no=int(input("Enter a number: "))
numberofbits(no)
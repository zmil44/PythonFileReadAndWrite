import random
def main():
    num1=random.randrange(0,101)
    num2=random.randrange(0,101)
    num3=random.randrange(0,101)
    fileOut=open('rand.txt','w')
    fileOut.write(str(num1)+'\n')
    fileOut.write(str(num2)+'\n')
    fileOut.write(str(num3)+'\n')
    fileOut.close()

    inFile=open('rand.txt','r')
    number1=int(inFile.readline())
    number2=int(inFile.readline())
    number3=int(inFile.readline())
    inFile.close()
    print(number1)
    print(number2)
    print(number3)
    
main()

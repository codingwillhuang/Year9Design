num = input("enter a number: ") # get user input using input() function
num = int(num) # converting or casting string to an integer

mylist = [1,2,3,4,5]
for n in mylist:
    if(n == num):
        print("you found it")
        break
    else:
        print(str(num) + " is not equal to " + str(n))
        
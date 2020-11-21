

def getDate():
    import datetime
    return datetime.datetime.now()


def HMS():

    def addData():
        print("1.Press 1 to log in Rohan's Routine")
        print("2.Press 2 to log in Shivansh's Routine")
        print("3.Press 3 to log in Aryan's Routine")

        choice1 = int(input("Enter your choice : "))

        if(choice1 == 1):
            print("********WELCOME TO ROHAN'S ROUTINE FILE********")
            print("1.Press 1 to log in diet chart.")
            print("2.Press 2 to log in exercise chart.")
            choice2 = int(input("Enter your choice : "))
            if(choice2 == 1):
                k = 'y'
                while(k != 'n'):
                    print("Enter your food : ")
                    food = input()
                    with open("Rohan_diet.txt", "a") as fp:
                        fp.write(f"{getDate()} : {food}\n")
                    print("Add more (y/n):", end="")
                    k = input()
                    continue
                print("Your Data has been Recorded...")
            elif(choice2 == 2):
                k = 'y'
                while(k != 'n'):
                    print("Enter your Exercise : ")
                    Exercise = input()
                    with open("Rohan_Exercise.txt", "a") as fp:
                        fp.write(f"{getDate()} : {Exercise}\n")
                    print("Add more (y/n):", end="")
                    k = input()
                    continue
                print("Your Data has been Recorded...")

        elif(choice1 == 2):
            print("********WELCOME TO SHIVANSH'S ROUTINE FILE********")
            print("1.Press 1 to log in diet chart.")
            print("2.Press 2 to log in exercise chart.")
            choice2 = int(input("Enter your choice : "))
            if(choice2 == 1):
                k = 'y'
                while(k != 'n'):
                    print("Enter your food : ")
                    food = input()
                    with open("Shivansh_diet.txt", "a") as fp:
                        fp.write(f"{getDate()} : {food}\n")
                    print("Add more (y/n):", end="")
                    k = input()
                    continue
                print("Your Data has been Recorded...")
            elif(choice2 == 2):
                k = 'y'
                while(k != 'n'):
                    print("Enter your Exercise : ")
                    Exercise = input()
                    with open("Shivansh_Exercise.txt", "a") as fp:
                        fp.write(f"{getDate()} : {Exercise}\n")
                    print("Add more (y/n):", end="")
                    k = input()
                    continue
                print("Your Data has been Recorded...")

        else:
            print("********WELCOME TO ARYAN'S ROUTINE FILE********")
            print("1.Press 1 to log in diet chart.")
            print("2.Press 2 to log in exercise chart.")
            choice2 = int(input("Enter your choice : "))
            if(choice2 == 1):
                k = 'y'
                while(k != 'n'):
                    print("Enter your food : ")
                    food = input()
                    with open("Aryan_diet.txt", "a") as fp:
                        fp.write(f"{getDate()} : {food}\n")
                    print("Add more (y/n):", end="")
                    k = input()
                    continue
                print("Your Data has been Recorded...")
            elif(choice2 == 2):
                k = 'y'
                while(k != 'n'):
                    print("Enter your Exercise : ")
                    Exercise = input()
                    with open("Aryan_Exercise.txt", "a") as fp:
                        fp.write(f"{getDate()} : {Exercise}\n")
                    print("Add more (y/n):", end="")
                    k = input()
                    continue
                print("Your Data has been Recorded...")

    def showData():
        print("1.Press 1 to see in Rohan's Routine")
        print("2.Press 2 to see in Shivansh's Routine")
        print("3.Press 3 to see in Aryan's Routine")

        choice1 = int(input("Enter your choice : "))
        if(choice1 == 1):
            print("1.Press 1 to see Rohan's Diet chart")
            print("2.Press 2 to see Rohan's Exercise chart")
            choice2 = int(input("Enter your choice:"))
            if(choice2 == 1):
                with open("Rohan_diet.txt") as fp:
                    print("********ROHAN'S DAILY DIET ********")
                    print(fp.read())
            else:
                with open("Rohan_Exercise.txt") as fp:
                    print("********ROHAN'S DAILY EXERCISE ********")
                    print(fp.read())

        elif(choice1 == 2):
            print("1.Press 1 to see Shivansh's Diet chart")
            print("2.Press 2 to see Shivansh's Exercise chart")
            choice2 = int(input("Enter your choice:"))
            if(choice2 == 1):
                with open("Shivansh_diet.txt") as fp:
                    print("********SHIVANSH'S DAILY DIET********")
                    print(fp.read())
            else:
                with open("Shivansh_Exercise.txt") as fp:
                    print("********SHIVANSH'S DAILY EXERCISE********")
                    print(fp.read())

        else:
            print("1.Press 1 to see Aryan's Diet chart")
            print("2.Press 2 to see Aryan's Exercise chart")
            choice2 = int(input("Enter your choice:"))
            if(choice2 == 1):
                with open("Aryan_diet.txt") as fp:
                    print("********ARYAN'S DAILY DIET********")
                    print(fp.read())
            else:
                with open("Aryan_Exercise.txt") as fp:
                    print("********ARYAN'S DAILY EXERCISE********")
                    print(fp.read())

    print("********WELCOME TO HEALTH MANAGEMENT SYSTEM**********")
    print("\n")
    print("1.Press 1 to Add the Records")
    print("2.Press 2 to see the Records")
    c = int(input("Enter your choice :"))
    if(c == 1):
        addData()
    else:
        showData()


HMS()

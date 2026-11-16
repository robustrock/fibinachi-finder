#1,1,2,3,5,8,13,21,etc
def fibinachi(length):
    #declaring useful variables
    previous_num = 0
    current_num = 1
    temp_num = 0

    #by returning the previous num and not the current puts the sequence back one whcih allows the user to put 0 and it to return 0 as in nothing!
    for i in range (length):
        temp_num = current_num
        current_num = current_num + previous_num
        previous_num = temp_num
    return(previous_num)


print("-------------fibinachi finder-------------")
while True:
    print("what digit of the fibinachi sequence would you like?(type exit to leave): ")
    user_in = input()

    if user_in == ("exit"):
        break

    try:
        user_in = int(user_in)

        if user_in < 0:
            print("please enter a possitive number!")
            continue
        print(fibinachi(user_in))

    except ValueError:
        print("Please enter a valid number!")

    
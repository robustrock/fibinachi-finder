#1,1,2,3,5,8,13,21,etc
def fibinachi(length):
    #declaring useful variables
    previous_num = 0
    current_num = 1
    temp_num = 0

    if(length) == (0):
        return(0)

    for i in range (length):
        temp_num = current_num
        current_num = current_num + previous_num
        previous_num = temp_num
    return(previous_num)

print(fibinachi(0))
print(fibinachi(1))
print(fibinachi(2))
print(fibinachi(3))
print(fibinachi(4))
print(fibinachi(5))
print(fibinachi(6))
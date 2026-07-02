marks = 80 # global variable 
def calculate_quota(total_marks):
    global sports # to access the global variable inside the function
    sports = True # local variable 
    if sports == True:
        return "Sports quota is applicable. And your new qualifying marks are 75"
    else:
        return "Sports quota is not applicable."
    

    
print(f'Your total marks are {marks}, Your status is {calculate_quota(marks)} and your sports quota status is {sports}.')


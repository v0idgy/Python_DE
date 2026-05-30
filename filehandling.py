# file = open('txt.txt', 'r') ## open the file in read mode
# content = file.read() ## read the content of the file
# print(content) ## print the content of the file





# with open('txt.txt', 'w') as file:
#     file.write("Hello this statement is writtten by write func.\n") ## write to the file
#     file.write("This is next statement.\n") ## write to the file


# print("Writing to the file is done.")



try:
    file = open('txt.txt', 'r')  ## open the file in read mode
    content = file.read() ## read the content of the file
    print(content) ## print the content of the file
except FileNotFoundError as e:
    print("File not found:", e)





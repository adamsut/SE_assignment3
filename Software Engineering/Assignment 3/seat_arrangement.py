Num_OccupiedSeats = 0
operation = ""
"""program which reads text file to calculate
    number of seats occupied in grid"""

#using nested for loops and lists create grid for chairs
grid = [[0 for x in range(1000)] for x in range(1000)]
for row in range(1000):
    for col in range(1000):
        grid[row][col] = 0

#read file
with open("C:\\Users\\user\\Desktop\\Comp Sci\\Semester 2\\Software Engineering\\Assignment 3\\input_assign3.txt","r") as f:
    for line in f:
        #for loop to recognise and attach command operations to each line of file
        if (line[:6] == "empty "):
            line = line[6:]
            operation  = "E"

        if (line[:6] == "toggle"):
            line = line[7:]
            operation  = "T"

        elif (line[:6] == "occupy"):
            line = line[7:]
            operation  = "O"



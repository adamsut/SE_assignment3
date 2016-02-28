import time
#import time

Num_OccupiedSeats = 0
operation = ""
"""program which reads text file to calculate
    number of seats occupied in grid"""
#intialise start time
start_time = time.time()
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

        #next, run through line breaking down each line into points (X1,X2,Y1,Y2)

        #remove and replace 'through' with ','
        line= line.replace(" through ",",")

        #use first readable comma as divider to seperate numbers
        divider = line.find(",")

        #find first number behind (:divisor) and set as first point.
        #follow along sequentially
        X1 = int(line[:divider])

        line = line[(divider + 1):]
        divider = line.find(",")
        Y1 = int(line[:divider])
        line = line[(divider + 1):]
        divider = line.find(",")
        X2 = int(line[:divider])
        line = line[(divider + 1):]
        Y2 = int(line)

        #go through line, then modifying grid by using an if statement process
        #using counter monitor the number of seats
        for row in range (X1, (X2+1)):
            for col in range(Y1, (Y2 + 1)):
                #processing statement
                if ( row % 100 == 0)& ( col % 100 == 0):
                    print 'processing..'


                if (operation == "E"):
                    if grid[row][col] != 0:
                        grid[row][col] = 0
                        if Num_OccupiedSeats  > 0:
                            Num_OccupiedSeats -= 1

                elif (operation == "O"):
                    if grid[row][col] != 1:
                        grid[row][col] = 1
                        if Num_OccupiedSeats  < 1000000:
                            Num_OccupiedSeats += 1

                else:
                    if (grid[row][col] == 1):
                        grid[row][col] = 0
                        if Num_OccupiedSeats  > 0:
                            Num_OccupiedSeats -= 1
                    else:
                        grid[row][col] = 1
                        if Num_OccupiedSeats  < 1000000:
                            Num_OccupiedSeats += 1
    print 'Execution Complete.'    #print number of occupied seats
    print("\nNumber of occupied seats: " + str(Num_OccupiedSeats))
    #print time for execution
    print '\nTime for execution:',(time.time()- start_time), 'seconds.'




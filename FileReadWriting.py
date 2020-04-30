#=====================================================


# this opens the file and reads all the line into a dictionary 
# like in a datbase the file has a primary key - the first piece of data on each line 
# this is unique for each line so we use it as the key in the dictionary 
def ReadFile(filename):

    # blank dictionary to store data in 
    data = {}

    # open the file in read mode 
    file = open(filename, "r")

    # for all the lines in the file 
    for line in file:
        
        # split up the data where there is a comma
        # this can be any symbol really 
        lineData = line.split(",")

        # if the line isn't empty 
        if len(lineData) > 1:
            
            # add that line to our data 
            data[lineData[0]] = [lineData[1], lineData[2]]

    #close the file 
    file.close()

    # return the data 
    return data


#============================================================


# this opens a file creates a backup of the data in the file 
# then adds the new data to the end of the backup 
# finally it overwrites the file 
def WriteFile(data, filename):

    # list to store the data in the file
    backup = []

    # will contain the data we want to add to the file
    toWrite = ""

    # open the file in read mode 
    file = open(filename, "r")
    
    # store every line of the file as a separate entry in the array
    backup = file.readlines()
    
    # close the file 
    file.close()

    # for each item in the data we want to write
    for item in data:

        # stick the items together as one string with commas separating them 
        toWrite = toWrite + item + ","
        
    # add the new data onto the end of the the backup from the file 
    # we have the new lines as separate enties that are written as well
    # so that our lines come out below one another 
    backup.append("\n")
    backup.append(toWrite)
    backup.append("\n")

    # open the file in write mode 
    file = open(filename, "w")
    
    # for each thing in backup 
    # these are all the lines we want to write into the file 
    for item in backup:

        # write that line into the file 
        file.write(item)
    
    # close the file 
    file.close()


#========================================================================


# testing the functions 
# with the included file 
students = ReadFile("Student.csv")

# this shows us all the data stored on the file 
for key in students:
    print("Student number {} | Student name {} | Address {}".format(key, students[key][0], students[key][1]))

# add some new data to the file 
WriteFile(["4", "Derick Hilado", "Some other place"], "Student.csv")

print("\n")

# show the data in the file now 
students = ReadFile("Student.csv")

for key in students:
    print("Student number {} | Student name {} | Address {}".format(key, students[key][0], students[key][1]))

input()


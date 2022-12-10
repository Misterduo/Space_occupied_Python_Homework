import os

#The following function counts all files in a given folder:
def folder_count_sum(folder):
    sum_folders = 0
    if os.path.isfile(folder):
        return 1
    else:
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                sum_folders += 1
            else:sum_folders += folder_count_sum(file_path)
    return sum_folders

#The following function counts the space occupied by the files:
def space_occupied_sum(folder):
    occupied_sum = 0
    if os.path.isfile(folder):
        return os.path.getsize(folder)
    else:
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                occupied_sum += os.path.getsize(file_path)
            else:occupied_sum += space_occupied_sum(file_path)
    return occupied_sum

#Please paste here the path to the file, so that the program can count the number of files and calculate their occupied size:
#For an example, please find the file with my previous homework as an example
my_folder = r'\spaceoccupied\venv\Check'

#Or use the following one, that requests the input from the user:
#folder = input(str("Please paste your desired path: "))
#my_folder = folder.replace(os.sep, '/')

print("< recursion in progress to count the total number of files >")
print("Count of all files in a given folder: " + str(folder_count_sum(my_folder)))

print("< recursion in progress to count the total space occupied by the files >")

#I have added space_occupied for the quicker future use in file size checker
space_occupied = space_occupied_sum(my_folder)

#Here, as I first checked the program with a file that was large ( it was in gigabytes ), I decided to add the below function
#To check and convert the size accordingly, to have a more visually appealing result
if int(space_occupied) >= 1000000000:
    print("Total space occupied by the files: " + str(int(space_occupied) * 0.000000001) + " gigabytes")
else:
    if int(space_occupied) < 1000000000 and int(space_occupied) >= 1000000:
        print("Total space occupied by the files: " + str(int(space_occupied) * 0.000001) + " megabytes")
    else:
        if int(space_occupied) < 1000000 and int(space_occupied) > 0:
            print("Total space occupied by the files: " + str(space_occupied) + " bytes")
        else: print("Total space occupied by the files: 0 bytes")
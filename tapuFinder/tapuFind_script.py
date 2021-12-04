import os
import shutil
import time

# Remove rest of TapuFindOd
directory = "/Users/Shared/"
foundThreat = False
threatsFound = 0
tempFile = ""
dirPath = '/Users/kaden/Library/LaunchAgents/'
fileName = 'TapufindOd.plist'
#print(40*"-")

# Remove TapufindOd.plist
# check if file is existing
print("> Checking for " + dirPath + fileName + "...")
time.sleep(1)
if os.path.isfile(dirPath + fileName):
    print("     > Removing file: " + dirPath + fileName + "...")
    os.remove(dirPath+fileName)
else:
    print("     > File '" + fileName + "' non existent")

print("")
time.sleep(1)
print("> Opening diectory '" + directory + "' ...")
os.chdir(directory)
time.sleep(1)

# iterate through every file in /Users/Shared/
for file in os.listdir("."):
    print("     > Checking directory '" + file + "' ...")
    time.sleep(0.5)

    # check if current file is a directory
    if os.path.isdir(directory + file):

        # change into the diectory and
        # iterate through each file in the dir
        os.chdir(directory+file)
        tempFile = file
        for file in os.listdir("."):
            # search for file
            if file.find("Tapufind") != -1 or file.find("tapufind") != -1:
                print("                 > Found bad directory... ")
                foundThreat = True
                threatsFound += 1
                break

        # if a file contains "Tapufind", delete the directory
        if foundThreat:
            print("                 > removing directory '" + tempFile + "' ...")
            time.sleep(2)
            shutil.rmtree(directory+tempFile)
            foundThreat = False

print(" ")
if threatsFound == 0:
    print("> Scanning '" + directory + "' finished: ")
    print("> No threatening directories found.")
else:
    print("> Scanning '" + directory + "' finished: ")
    print("> " + str(threatsFound) + " threatening directories removed.")

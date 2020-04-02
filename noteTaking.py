import os
noteFile = input("What file do you want to take notes in?\n\n")
fileExist = os.path.isfile(noteFile)

def takeMyNotes(file, type):
    myNotes = open(file,type)
    print("To stop taking notes type \"I am done\" and press the Enter key.\n")
    while True:
        userTypes = input()
        if userTypes == "I am done":
            break
        myNotes.write(userTypes + "\n")
        print("")
    myNotes.close()

if fileExist == False:
    print("That's a new file, but lets takes some notes!\n")
    myNewFile = "w"
    takeMyNotes(noteFile, myNewFile)
else:
    prevNotes = input("What would you like to do to those Notes?\n\nA) Read the File\nB) Delete and start over\nC) Append the file\n\n")
    if prevNotes == "Read the File":
        readFile = open(noteFile, "r")
        print("\n" + readFile.read())
    elif prevNotes == "Delete and start over":
        print("Okay. Lets take some new Notes!\n")
        deletedFile = "w"
        takeMyNotes(noteFile, deletedFile)
    else:
        appendFile = "a"
        takeMyNotes(noteFile, appendFile)

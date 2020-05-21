print("This code is an example of the functionality of FileIO. As you run the code, it will puase at parts after the specifics have been executed.")
proceed = input("It is encouraged that after every stop, you go back to Animal_Farm.txt and see what changes were made to the file itself. If you understand type, yes")
if proceed == "yes":

    # simple print output
    ask = input("Do you want to do a simple print command? (yes, no)")
    if ask == "yes":
        print("Python is cool")  # prints "Python is cool"

    # reading keyboard input
    ask = input("Do you want the code to echo what you type? (yes,no)")
    if ask == "yes":
        str = input("enter your input")  # reads the input and saves it as a variable
        print(str)  # prints the variable

    # opening files
    ask = input("Do You want to display info about the file? (yes, no)")
    if ask == "yes":
        fo = open("Animal_Farm.txt")  # opens the file in reading only (default mode)
        print("Name of the file: ", fo.name)  # prints the name of the file (Animal Farm)
        print("closed on not: ", fo.closed)  # prints if the file is closed or not (true means closed, false means open)
        print("Opening Mode: ", fo.mode)  # tells what mode the file is open in (defaults to read, r)

    # Appending Files
    ask = input("Do you want to append a sentance at the end of the File? (yes,no)")
    if ask == "yes":
        fo = open("Animal_Farm.txt", "a")  # opens the File for Appending
        fo.write("written by George Orwell")  # Appends the phrase "written by George Orwell" at the bottom

    # reading files
    ask = input("Do you want to read the first 1000 bytes of the file? (yes, no)")
    if ask == "yes":
        fo = open("Animal_Farm.txt",
                  "r+")  # opens the file for reading AND the bianary format so you can read bytes as well
        str = fo.read(1000);  # reads the first 1000 bytes of the file ans stores it in a variable as str
        print(str)  # prints the variable

    # Writing in Files
    ask = input(
        "Do you want to Write the file? WARNING: this will delete all of the text and replace it with the text in the code (yes, no)")
    if ask == "yes":
        fo = open("Animal_Farm.txt", "w")  # opens the file for writing only and deletes the contents by defalut
        fo.write("Everything is gone mwahahahahaha")  #Writes "Everything is gone mwahahahahaha"

    # closes the file at the end
    fo.close()

# If you want to experiment more, the full txt of Anmimal Farm is in
#Default_Animal_Farm.txt
# you can copy and paste the file into Animal_Farm.txt to get a clean slate




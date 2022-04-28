import json

def main():
    with open("database.json", "r") as read_file: # open an external file and put into 'read_file' variable
        database = json.load(read_file) # pass the raw json data into python so we can use it properly

    name = input("please name your character: ")
    death= "\n \n YOU ARE DEAD"
    error = "I'm sorry, I didn't catch that. Please select a path by choosing the appropriate letter."

    def branch(branch_num): # create a reusable function for branches
        db_object = database["branches"][branch_num - 1] # find the branch in the branches array that we want to interact with

        selection = input(db_object["branch"] + " ") # create an input field with the initial message from the 'branch' item in the database 

        if selection.upper() in db_object["options"]: # if the users selection is a valid option in the 'options' array in the database
            print(db_object["messages"][db_object["options"].index(selection.upper())]) # print the message that matches the same array index of the option selected (and use .upper() to make sure they match when comparing)

            if selection.upper() == db_object["correct_branch"]: # if the selection is the correct branch as defined in the database
                # return True
                branch(branch_num + 1) # move on to the next branch (inconsiderate to whether one actually exists)
        else: # if the users selection is NOT a valid option from the database
            print(error + "\n") # print the pre-defined error msg
            main() # restart back to the top

    branch(1) # start the chain of branches at the first one
main() # start the entire program

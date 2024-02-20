


NUMBER_OF_ROWS = 5


def get_input(prompt, arr):
    while True:
        usr_input = input(prompt)
        if usr_input in arr:
            return usr_input
        print("That was not valid, options are", arr)
    


def doShit():
    run = True
    questions = []
    file = open("questions.txt", "w")

    for cols in range(6):
        q_type = get_input("What type of 5 questions do you want to add?  -  ", ["quote", "theme", "visual", "connections"])
        if q_type == "quote":
            for rows in range(1, NUMBER_OF_ROWS+1):
                quote = input("Please enter a quote: ")
                ans = input("Please enter an answer: ")
                value = rows*100
                file.write(str("quote," + quote + "," + ans + "," + str(value) + "\n"))

        if q_type == "theme":
            for rows in range(1, NUMBER_OF_ROWS+1):
                theme = input("Please enter an mp3 file path: ")
                ans = input("Please enter an answer: ")
                value = rows*100
                file.write(str("theme," + theme + "," + ans + "," + str(value) + "\n"))

        if q_type == "visual":
            for rows in range(1, NUMBER_OF_ROWS+1):
                visual = input("Please enter an image path to reverse dissolve : ")
                ans = input("Please enter an answer: ")
                value = rows*100
                file.write(str("visual," + visual + "," + ans + "," + str(value) + "\n"))

        if q_type == "connections":
            for rows in range(1, NUMBER_OF_ROWS+1):
                square1 = input("Please enter the first connection: ")
                square2 = input("Please enter the second connection: ")
                square3 = input("Please enter the third connection: ")
                square4 = input("Please enter the fourth connection: ")
                ans = input("Please enter an answer: ")
                value = rows*100
                file.write(str("connection," + square1 + "," + square2 + "," + square3 + "," + square4 + "," + ans + "," + str(value) + "\n"))

    file.close()





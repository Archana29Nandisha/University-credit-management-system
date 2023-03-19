#I declare that my work contains no examples of misconduct, such as plagiarism, or
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20211438
# Date: 04/08/2022

Prog_count = 0
Trail_count = 0
Retr_count = 0 
Excl_count = 0

while True:
    while True:
        Pass = (input("Please enter your credits at Pass: "))
        if Pass.isnumeric():  # https://www.programiz.com/python-programming/methods/string/isnumeric
            if int(Pass) in range(0, 121, 20):
                break
            else:
                print("Out of range")
        else:
            print("Integer required")

    while True:
        Defer = (input("Please enter your credits at Defer: "))
        if Defer.isnumeric():
            if int(Defer) in range(0, 121, 20):
                break
            else:
                print("Out of range")
        else:
            print("Integer required")

    while True:
        Fail = (input("Please enter your credits at Fail: "))
        if Fail.isnumeric():
            if int(Fail) in range(0, 121, 20):
                break
            else:
                print("Out of range")
        else:
            print("Integer required")


    def horizontal_histogram():
        print("Horizontal Histogram ")
        print(
            f"Progress {Prog_count}  : " + "*" * Prog_count)  # https://www.programiz.com/python-programming/methods/string/format
        print(f"Trailer {Trail_count}  : " + "*" * Trail_count)
        print(f"Retriever {Retr_count}  : " + "*" * Retr_count)
        print(f"Exclude {Excl_count}  : " + "*" * Excl_count)
        total_count = (Prog_count + Trail_count + Retr_count + Excl_count)
        print(f"{total_count} outcomes in total")


    if int(Pass) + int(Defer) + int(Fail) == 120:
        if int(Pass) == 120:
            Prog_count = Prog_count + 1
            print("Progress")

        if int(Pass) == 100:
            if int(Defer) in range(0, 21, 20):
                Trail_count = Trail_count + 1
                print("Progress (Module Trailer)")

        if int(Pass) in range(0, 41, 20):
            if int(Fail) in range(80, 121, 20):
                Excl_count = Excl_count + 1
                print("Exclude")

        if int(Pass) in range(0, 81, 20):
            if int(Fail) in range(0, 61, 20):
                Retr_count = Retr_count + 1
                print("Do not Progress- Module retriever")

    else:
        print("Total incorrect")
    question = ""
    while question != "y" and question != "q":
        print("Would you like to enter another set of data? ")
        question = input("Enter 'y' for yes or 'q' to quit and view results: ")

    if question == "q":
        horizontal_histogram()
        break

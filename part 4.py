# I declare that my work contains no examples of misconduct, such as plagiarism, or
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20211438
# Date: 04/11/2022

Prog_count = 0
Trail_count = 0
Retr_count = 0
Excl_count = 0

progress_list = []
module_trailer_list = []
module_retriever_list = []
Exclude_list = []


while True :
    while True :
        Pass = (input("Please enter your credits at Pass: "))
        if Pass.isnumeric() :   #https://www.programiz.com/python-programming/methods/string/isnumeric
            if int(Pass) in range(0,121,20):
                break
            else:
             print("Out of range")
        else :
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

    if int(Pass) + int(Defer) + int(Fail) == 120 :
        if int(Pass) == 120:
            Prog_count = Prog_count + 1
            progress_list.append(f"{Pass}, {Defer}, {Fail}")  #https://www.programiz.com/python-programming/methods/string/format
            print("Progress")

        if int(Pass) == 100:
            if int(Defer) in range(0, 21, 20):
                Trail_count = Trail_count + 1
                module_trailer_list.append(f"{Pass}, {Defer}, {Fail}")
                print("Progress (Module Trailer)")

        if int(Pass) in range(0, 41, 20):
            if int(Fail) in range(80, 121, 20):
                Excl_count = Excl_count + 1
                Exclude_list.append(f"{Pass}, {Defer}, {Fail}")
                print("Exclude")

        if int(Pass) in range(0, 81, 20):
            if int(Fail) in range(0, 61, 20):
                Retr_count = Retr_count + 1
                module_retriever_list.append(f"{Pass}, {Defer}, {Fail}")
                print("Do not Progress- Module retriever")

    else:
        print("Total incorrect")
    question = ""
    while question != "y" and question != "q" :
        print("Would you like to enter another set of data? ")
        question = input("Enter 'y' for yes or 'q' to quit and view results: ")

    if question == "q":
        print("...............................................................")
        print("  ")

        document_file = open("Python_text", "w")

        for i in progress_list:
            document_file.write(f"Progress - , {i}  \n")

        for i in module_trailer_list:
            document_file.write(f"Progress (module trailer) - ,  {i}  \n")

        for i in module_retriever_list:
            document_file.write(f"Module retriever - , {i}  \n")

        for i in Exclude_list:
            document_file.write(f"Exclude - , {i}  \n ")
        break

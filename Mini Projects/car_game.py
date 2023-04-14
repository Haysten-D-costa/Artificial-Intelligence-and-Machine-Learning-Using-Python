started = False
operation = ""

while True:
    operation = input("> ")
    if operation.lower() == "help":
        print('''
            START -> To start the car
            STOP  -> To stop the car
            QUIT  -> To exit / terminate the program
        ''')
    elif operation.lower() == "start":
        if started == True:
            print("Car already started...\n")
        else:
            started = True
            print("Car started...\n")
    elif operation.lower() == "stop":
        if not started:
            print("Car not started...\n")
        else:
            started = False
            print("Car stopped...\n")
    elif operation.lower() == "quit":
        break
    else:
        print("No such functionality...\n")

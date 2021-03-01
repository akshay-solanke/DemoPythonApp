command = ""
Car_started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if Car_started:
            print('Car already started')
        else:
            print('Car Started')
            Car_started = True
    elif command == "stop":
        if not Car_started:
            print('Car already stopped')
        else:
            print('Car Stopped')
            Car_started = False
    elif command == "help":
        print("""
start = To start the car
stop = To stop the car
quit = To exit
        """)
    elif command == "quit":
        break
    else:
        print("i don't understand !")

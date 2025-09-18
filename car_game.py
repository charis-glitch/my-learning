started = False  #"starded = True" means, from the very beginning of the program, the car is already marked as started. So every time you type "start", the code only checks "if started": (which is always True) → and it never updates started.
while True:
    type = input("> ").lower()
    if type == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit 
              """)
    elif type == "start":
        if started: #if started: means "if started == True"; "if started" is False → the code inside if is skipped
            print("car has already started")
        else:
            print("car started... ready to go")
            started = True  #let "started = False" run once and set it to Ture, so "car started" print once, then it's "car already..." forever
    elif type == "stop":
        if not started: #"started" is True, because car starts first, in "start" the "started" has been turned into True
            print("car has already stopped")
        else:
            print("car stopped")
            started = False
    elif type == "quit":
        break
    else:
        print("i don't understand that...")
# "started" changes over time. Typing "start" sets it to True. Typing "stop" sets it to False. It’s acting like a little state variable that remembers whether the car is running or not.
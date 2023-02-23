while True:                         #To make it go in loop untill try works
    try: 
        answer = float(input("how many hours did you work? "))  #when character is given as input, code giver error. 
                                                            #To avoid, we'll use try. Also, input always gives str
        
        payrate = float(input("what is your pay rate?"))
        paycheck = answer*payrate
        print(f"Your total pay is: ${paycheck}")
        break                                   #to break loop once try works
    except ValueError as err:
        #pass                                   #pass is used to pass if try doesn't work
        print(f"There was an error: {err}")
   
halt =""
is_started = False

while (halt != 'quit'):    
    your_option = input(f'Your option:')
    if (your_option.lower()=="start"):
        if (is_started==False):
            print(f'"Car started')
            is_started = True
        elif (is_started == True):
            print(f'"Car ALREADY started')
    elif (your_option.lower()=="stop" and is_started==False):
        print(f'"Car not started, please start the car first!')
    elif (your_option.lower()=="stop" and is_started==True):
        print(f'"Car stopped!')
        is_started = False    
    elif (your_option.lower()=="help"):        
        print(f''''"start" to start the Car'
'"stop" to stop the Car'
'"quit" to Quit the Game''')        
    elif (your_option.lower()=="quit"):
        print(f'"Game Over')
        break
    else:
        print(f'''Sorry, I don't understand that, 
    Please Enter meaningfull options like "help"''')
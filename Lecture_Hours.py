WeekHours = 0
Week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        
while True:    
    # User chooses day
    user_choice = int(input('Choose your day: \n 0. Monday \n 1. Tuesday \n 2. Wednesday \n 3. Thursday \n 4. Friday \n ( 0, 1 , 2 , 3 , or 4) \n') )     
    
    if user_choice in [0, 1, 2, 3, 4]:             # Verify user input with given numbers 
        
        print(f"Its {Week[user_choice]}. Full day class")        
        WeekHours += 3
        
        print(f"You had {WeekHours} lecture hours this week. \n") 

    else:                                           # Prints invalid user input
        invalid_choice = '{} is invalid. '
        print(invalid_choice.format(user_choice))          
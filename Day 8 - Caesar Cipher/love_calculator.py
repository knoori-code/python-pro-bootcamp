def calculate_love_score(name1, name2):
    true_string = 'true'
    true_counter = 0
    love_string = 'love'
    love_counter = 0
    combined_name = name1 + name2
    
    for letter in combined_name:
        if letter in true_string:
            true_counter += 1
        if letter in love_string:
            love_counter += 1
            
    love_score = str(true_counter) + str(love_counter)
    
    print(love_score)
    
calculate_love_score(name1="Jay-Z", name2="Beyonce")
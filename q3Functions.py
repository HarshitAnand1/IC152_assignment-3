def perfect_num_checker(): 
    num_list = [6, 2, 20, 496, 30, 8128, 500, 1000, 33550336, 999983]
    
    for num in num_list: 
        div_sum = 0
        
        for i in range(1,((num//2)+1)): 
            if num%i==0:
                div_sum = div_sum +i
                
        if div_sum == num: 
            print(f"{num} is a pefect number") 
        else: 
            print(f"{num} is not a pefect number")
            
perfect_num_checker()

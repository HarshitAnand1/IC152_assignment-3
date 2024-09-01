def perfect_num_checker():
    n = int(input("Enter a number: "))

    div_sum = 0
    for i in range (1, n//2 + 1):
        if n//i == n/i:
            div_sum = div_sum +i
    
    if div_sum == n:
        print("The given number is a pefect number")
    else:
        print("The given number is not a pefect number")

perfect_num_checker()
# Part a

# using for loops
def inv_tri_for():
    n1 = int(input("q4 part a input (integer): "))
    for i in range(n1):
        print(f"{' '* i} {'*' * (n1-i)}")


# using while loops
def inv_tri_while():
    n2 = int(input("q4 part a input (integer): "))

    i =0
    while i < n2:
        print(f"{' '* i} {'*' * (n2-i)}")
        i +=1

# Part b
# using for loop
def alpha_tri_for():
    n3 = int(input("q4 part b input (integer): "))
    for i in range(1,n3+1):
        for j in range (i):
            print(chr(j+65), end="")
        print("")

# using while loop
def alpha_tri_while():
    n4 = int(input("q4 part b input (integer): "))

    i = 1
    while i <= n4:
        j = 0
        while j < i:
            print(chr(j+65), end="")
            j+=1
        print("")   
        i+=1


inv_tri_for()
inv_tri_while()
alpha_tri_for()
alpha_tri_while()
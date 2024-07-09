# Permutation && Combination Calculator by @noulion on github!
import time
import os



p = "P(n,r) = n!/(n-r)!"
c = "C(n, r) = n!/(n−r)!r!"

#Math Functions
def factorial(a):
    try:
        b = factorial
        if a <= 2:
            return a
        else:
            return a * b(a-1)
    except RecursionError:
        return abs(a)
    

def permutation(a, b):
    try:
        if a and b <= 2:
            return a and b
        else:
            return factorial(a) / factorial(a-b)
    except ZeroDivisionError as e:
        return 0
    except OverflowError:
        return abs(a) / abs(b)
        
def combination(n, r):
    try:
        if n and r == 1:
            return n and r
        else:
            return factorial(n) / (factorial(n-r))/(factorial(r))
    except ZeroDivisionError:
        os.system('clear')
        return 0 
        
#All of the visuals are here:
def calculator_base():
    
    #Calculator of combination:
    def calculator_combi():
        a = 0
        b = 0
        print(c)
        
        #if value of a, b are filled then this function is called.
        def combi_solve(a, b):
            print(c)
            print(" \nFormula is ready\n")
            print(f"C({a}, {b}) = {a}!/({a}−{b})!{b}", end=" ")
            
            while True:
                 start_solve = input("[Press enter to solve]\r")
                 
                 #Only start if a space or enter is entered.
                 if start_solve == '':
                     os.system('clear')
                     ans = combination(a, b)
                     
                     print(c)
                     print(f"\nSolved!\n")
                     print(f"C({a}, {b}) = {a}!/({a}−{b})!{b}\n= C({ans})\n")
                     print("\n\nreturning..")
                     time.sleep(2.7)
                     os.system('clear')
                     return calculator_base()
                     break
                 
                 #else, just return to solving menu.
                 else:
                     print('\njust click enter..')
                     os.system('clear')
                     return combi_solve(a, b)
        
        # (n) value input:
        print("\nput a value for 'n'\n")
        while a >= 0:
            try:
                a_in = int(input(f"C({a}, {b}) = {a}!/({a}−{b})!{b}!: "))
                
                if a_in == a_in:
                    a+=a_in
                    os.system('clear')
                    break
            except ValueError:
                print("Numbers Only")
        # (r) value input:
        print(c)
        print("\nput a value for 'r'\n")
        while b <= 0:
            try:
                b_in = int(input(f"C({a}, {b}) = {a}!/({a}−{b})!{b}!: "))
                
                if b_in == b_in:
                    b+=b_in
                    os.system('clear')
                    return combi_solve(a, b)
                    break
            except ValueError:
                print("Numbers Only")
    #Calculator of permutation:
    def calculator_permu():
         a = 0
         b = 0
         print(p)
         
         #if value a,b are filled then this function is called.
         def permu_solve(a, b):
             print(p)
             print(" \nFormula is ready\n")
             print(f"P({a},{b}) = {a}!/({a}-{b})!", end=" ") #New filled formula.
             
             #Asks user if he wants to solve the filled formula.
             while True:
                 start_solve = input("[Press enter to solve]\r")
                 
                 #Only start if a space or enter is entered.
                 if start_solve == '':
                     os.system('clear')
                     ans = permutation(a, b)
                     
                     print(p)
                     print(f"\nSolved!\n")
                     print(f"P({a},{b}) = {a}!/({a}-{b})! \n= P({ans})\n")
                     print("\n\nreturning..")
                     time.sleep(2.7)
                     os.system('clear')
                     return calculator_base()
                     break
                 
                 #else, just return to solving menu.
                 else:
                     print('\njust click enter..')
                     os.system('clear')
                     return permu_solve(a, b)
         
         # (n) value input:
         print("\nput a value for 'n'\n")
         while a >= 0:
             try:
                 a_in = int(input(f"P({a},{b}) = {a}!/({a}-{b})!: "))
                 
                 if a_in == a_in:
                     a+=a_in
                     os.system('clear')
                     break
             except ValueError:
                 print("Numbers Only...")
                 
         # (r) value input:
         print(p)
         print(" \nput a value for 'r'\n")  
         while b >= 0:
             try:
                 b_in = int(input(f"P({a},{b}) = {a}!/({a}-{b})!: "))
                 
                 if b_in == b_in:
                     b+=b_in
                     os.system('clear')
                     return permu_solve(a, b)
                     break
                     
             except ValueError:
                 print("\nNumbers Only...\n")
    
    #main calculator-menu:         
    def calculator_menu():
        print("[Permutation \\ Combination Calculator]\n") #Logo.
        print(f"Permutation Formula = {p}\nCombination Formula = {c}\n\n") #Formulas.               
        calculator_options = {1:'Permutation',
                              2:'Combination',
                              3:'Exit'
        }
        
        for num,option in calculator_options.items():
            print(f' ({num}) -▷ {option}')
        
        while True:
            calc_input = input("\n; ")
            
            if calc_input == '1':
                os.system('clear')
                return calculator_permu()
                break
                
            elif calc_input == '2':
                os.system('clear')
                return calculator_combi()
                break
            
            elif calc_input == '3':
                print("\nExited with 0..")
                break
                
            else:
                os.system('clear')
                return calculator_menu()
        
    calculator_menu()
   
calculator_base()calculator_base()

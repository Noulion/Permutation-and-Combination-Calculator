# Permutation && Combination Calculator by @noulion on github!
import time
import os
import math 

p = "__P(n,r) = n!/(n-r)!__"
c = "__C(n, r) = n!/(n−r)!r!__"

#Math Functions
def factorial(a):
    b = factorial
    if a < 2:
        return a
    else:
        return a * b(a-1)

def permutation(a, b):
    if a and b <= 2:
        return a and b
    else:
        return factorial(a) / factorial(a-b)
        
def combination(n, r):
    if n and r == 1:
        return n and r
    else:
        return factorial(n) / (factorial(n-r))/(factorial(r))
        
        
#All of the visuals are here:
def calculator_base():
    
    #Calculator of combination:
    def calculator_combi():
        return calculator_base() #temporary.
    
    #Calculator of permutation:
    def calculator_permu():
         a = 0
         b = 0
         print(p)
         
         #if value a,b are filled then this function is called.
         def permu_solve(a, b):
             print(p)
             print("Formula is ready\n")
             print(f"P({a},{b}) = {a}!/({a}-{b})!\n\n") #New filled formula.
             
             #Asks user if he wants to solve the filled formula.
             while True:
                 start_solve = input("[Press enter to solve]\r")
                 
                 #Only start if a space or enter is entered.
                 if start_solve == '':
                     os.system('clear')
                     ans = permutation(a, b) 
                     
                     print(p)
                     print(f"Solved!\n\n")
                     print(f"P({a},{b}) = {a}!/({a}-{b})! = {ans}\n\n")
                     print("returning..")
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
         print("put a value for 'n'\n")
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
         print("put a value for 'r'\n")  
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
        print("[Permutation & Combination Calculator]\n") #Logo.
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
                
            if calc_input == '2':
                os.system('clear')
                return calculator_combi()
                break
            
            if calc_input == '3':
                print("\nExited..")
                break
                
            else:
                os.system('clear')
                return calculator_menu()
        
    calculator_menu()
   
calculator_base()
from selectors import SelectSelector

print(r'''
     __                                                      
     /  l                                                     
   .'   :               __.....__..._  ____                   
  /  /   \          _.-"        "-.  ""    "-.                
 (`-: .---:    .--.'          _....J.         "-.             
  """y     \,.'    \  __..--""       `+""--.     `.           
    :     .'/    .-"""-. _.            `.   "-.    `._.._     
    ;  _.'.'  .-j       `.               \     "-.   "-._`.   
    :    / .-" :          \  `-.          `-      "-.      \  
     ;  /.'    ;          :;               ."        \      `,
     :_:/      ::\        ;:     (        /   .-"   .')      ;
       ;-"      ; "-.    /  ;           .^. .'    .' /    .-" 
      /     .-  :    `. '.  : .- / __.-j.'.'   .-"  /.---'    
     /  /      `,\.  .'   "":'  /-"   .'       \__.'          
    :  :         ,\""       ; .'    .'      .-""              
   _J  ;         ; `.      /.'    _/    \.-"                  
  /  "-:        /"--.b-..-'     .'       ;                    
 /     /  ""-..'            .--'.-'/  ,  :                    
:`.   :     / : bug         `-i" ,',_:  _ \                   
:  \  '._  :__;             .'.-"; ; ; j `.l                  
 \  \          "-._         `"  :_/ :_/                       
  `.;\             "-._                                       
    :_"-._             "-.                                    
      `.  l "-.     )     `.                                  
        ""^--""^-. :        \                                 
                  ";         \                                
                  :           `._                             
                  ; /    \ `._   ""---.                       
                 / /   _      `.--.__.'                       
                : :   / ;  :".  \                             
                ; ;  :  :  ;  `. `.                           
               /  ;  :   ; :    `. `.                         
              /  /:  ;   :  ;     "-'                         
             :_.' ;  ;    ; :                                 
                 /  /     :_l                                 
                 `-'                                  
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice_one = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if choice_one == "left":
    choice_2 = input("You've come to a lake. There is an island in the middle of the lake. "
                     "Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()

    if choice_2 == "wait":
        choice_3 = input("You arrive safely on the island. There is a house with three doors: one red, one yellow, and one blue. "
                         "Which color do you choose? ").lower()

        if choice_3 == "red":
            print("This room is on fire. You are dead. Game Over.")
        elif choice_3 == "yellow":
            print("You found the treasure! Congratulations!")
        elif choice_3 == "blue":
            print("This room has two very hungry lions. They ate you! Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("A shark just ate you. Game Over.")
else:
    print("You fell into a hole. Game Over.")
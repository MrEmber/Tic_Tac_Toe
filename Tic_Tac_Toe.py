from Tic_Tac_Data import Tic_Tac_Data 
empty_tic_tac_template = """
                   |       |   
              {0}    |   {1}   |   {2}
          _________|_______|_______
                   |       |
              {3}    |   {4}   |   {5}
           ________|_______|_______
                   |       |  
              {6}    |   {7}   |  {8}
                   |       |
    """
class Tic_Tac_Data:
    def __init__(self):
        pass
    def __repr__(self):
        return empty_tic_tac_template

tic_tac_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
empty_lst = empty_tic_tac_template.format(*tic_tac_list)
#Font Used "Doom"
print(""" 
 _____ _        _____            _____          
|_   _(_)      |_   _|          |_   _|         
  | |  _  ___    | | __ _  ___    | | ___   ___ 
  | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ |
  | | | | (__    | | (_| | (__    | | (_) |  __/
  \_/ |_|\___|   \_/\__,_|\___|   \_/\___/ \___|
""")
#
print("")
print("         Welcome to Tic Tac Toe Version 1.0!         ")
print(empty_lst)
print("")
print("     Player 1 which space would you like to place?         ")
#Start page ^^^
player_one_in = input(">>> ")

try:
    if int(player_one_in) in range(1,10):
        print("works")
    else:
        print("""
        
         _   _ _             _           
        | | | | |           | |          
        | | | | |__     ___ | |__        
        | | | | '_ \   / _ \| '_ \       
        | |_| | | | | | (_) | | | |_ _ _ 
         \___/|_| |_|  \___/|_| |_(_|_|_)
    """)
        print("""
    
         Looks like your response was invalid 
    
    Please type in the number of the sqaure you want to place. 
                    Examples:
         "1" "2" "3" "4" "5" "6" "7" "8" "9"
    """)
        print(empty_lst)
except ValueError:
    print("""
        
         _   _ _             _           
        | | | | |           | |          
        | | | | |__     ___ | |__        
        | | | | '_ \   / _ \| '_ \       
        | |_| | | | | | (_) | | | |_ _ _ 
         \___/|_| |_|  \___/|_| |_(_|_|_)
    """)
    print("""
    
         Looks like your response was invalid 
    
    Please type in the number of the sqaure you want to place. 
                    Examples:
         "1" "2" "3" "4" "5" "6" "7" "8" "9"
    """)

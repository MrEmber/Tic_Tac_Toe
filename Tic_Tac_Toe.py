
from re import T


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
invalid_response = """
        
                  _   _ _             _           
                 | | | | |           | |          
                 | | | | |__     ___ | |__        
                 | | | | '_ \   / _ \| '_ \       
                 | |_| | | | | | (_) | | | |_ _ _ 
                  \___/|_| |_|  \___/|_| |_(_|_|_)
             

    
                Looks like your response was invalid 
    
         Please type in the number of the sqaure you want to place. 
                           Examples:
              "1" "2" "3" "4" "5" "6" "7" "8" "9"
              >>> """

class Tic_Tac_Data:
    def __init__(self):
        pass
    
    

    def __repr__(self):
        return empty_tic_tac_template

tic_tac_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
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
print("""
                   |       |   
              1    |   2   |   3
          _________|_______|_______
                   |       |
              4    |   5   |   6
           ________|_______|_______
                   |       |  
              7    |   8   |  9
                   |       |
    """)
print("")
turn = 0
for x in tic_tac_list:
    if x == " ":
     turn += 1
#Start page ^^^
class Game_Init:
    
    def win_checker(self):
        if (tic_tac_list[0] == "X" and tic_tac_list[1] == "X" and tic_tac_list[2] == "X") or (tic_tac_list[0] == "X" and tic_tac_list[3] == "X" and tic_tac_list[6] == "X") or (tic_tac_list[2] == "X" and tic_tac_list[5] == "X" and tic_tac_list[8] == "X") or (tic_tac_list[6] == "X" and tic_tac_list[7] == "X" and tic_tac_list[8] == "X") or (tic_tac_list[0] == "X" and tic_tac_list[4] == "X" and tic_tac_list[9] == "X") or (tic_tac_list[2] == "X" and tic_tac_list[4] == "X" and tic_tac_list[6] == "X"):
            print("Player 1 has won")

        elif (tic_tac_list[0] == "O" and tic_tac_list[1] == "O" and tic_tac_list[2] == "O") or (tic_tac_list[0] == "O" and tic_tac_list[3] == "O" and tic_tac_list[6] == "O") or (tic_tac_list[2] == "O" and tic_tac_list[5] == "O" and tic_tac_list[8] == "O") or (tic_tac_list[6] == "O" and tic_tac_list[7] == "O" and tic_tac_list[8] == "O") or (tic_tac_list[0] == "O" and tic_tac_list[4] == "O" and tic_tac_list[9] == "O") or (tic_tac_list[2] == "O" and tic_tac_list[4] == "O" and tic_tac_list[6] == "O"):
            print("Player 1 has won")

        else:
            pass
        
    while turn >= 0:
            if turn % 2 != 0:
                player_one_in = input("""
                Player 1 which space would you like to place?         
                >>> """)
                try:
                    if int(player_one_in) in range(1,10):
                        if tic_tac_list[int(player_one_in)-1] == " ":
                            print("")
                            tic_tac_list[int(player_one_in)-1] = "X"
                            empty_lst = empty_tic_tac_template.format(*tic_tac_list)
                            print(empty_lst)
                            
                            win_checker(tic_tac_list)
                            turn += 1
                        elif tic_tac_list[int(player_one_in)-1] == "O":
                            print("""
                
                            _   _ _             _           
                            | | | | |           | |          
                            | | | | |__     ___ | |__        
                            | | | | '_ \   / _ \| '_ \       
                            | |_| | | | | | (_) | | | |_ _ _ 
                            \___/|_| |_|  \___/|_| |_(_|_|_)
                    

            
                            Looks like player 2 has already gone their""")
                            if int(player_one_in) in range(1,10):
                                if tic_tac_list[int(player_one_in)-1] == " ":
                                    print("")
                                    tic_tac_list[int(player_one_in)-1] = "X"
                                    empty_lst = empty_tic_tac_template.format(*tic_tac_list)
                                    print(empty_lst)
                                    turn -= 1
                        else:
                            print(invalid_response)
                            player_one_in = input("""
                            Press any key to Continue
                            >>> """)
                            
                except ValueError:
                    print(invalid_response)
                
            elif turn % 2 == 0:
                player_two_in = input("""
                Player 2 which space would you like to place?         
                >>> """)
                try:
                    if int(player_two_in) in range(1,10):
                        if tic_tac_list[int(player_two_in)-1] == " ":
                            print("")
                            tic_tac_list[int(player_two_in)-1] = "O"
                            empty_lst = empty_tic_tac_template.format(*tic_tac_list)
                            print(empty_lst)
                            
                            win_checker(tic_tac_list)
                            turn += 1
                        elif tic_tac_list[int(player_one_in)-1] == "X":
                            print("""
                
                            _   _ _             _           
                            | | | | |           | |          
                            | | | | |__     ___ | |__        
                            | | | | '_ \   / _ \| '_ \       
                            | |_| | | | | | (_) | | | |_ _ _ 
                            \___/|_| |_|  \___/|_| |_(_|_|_)
                        

            
                            Looks like player 1 has already gone their""")
                        
                            if tic_tac_list[int(player_two_in)-1] == " ":
                                print("")
                                tic_tac_list[int(player_two_in)-1] = "O"
                                empty_lst = empty_tic_tac_template.format(*tic_tac_list)
                                print(empty_lst)
                                turn -= 1
                            
                    


                        else:
                            print(invalid_response)
                            player_two_in = input("""
                            Press any key to continue >>> """)
                            
                except ValueError:

                    print(invalid_response)
                    
    win_checker(tic_tac_list)                  
        

    
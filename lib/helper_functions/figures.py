import time

def show_store():
    figure = '''
__________________________________________________________________
           |                       |                              |
           |    F L A T S T O P    |______________________________|
|__________|_______________________|_________||_|_|_|_|_|_|_|_|_|_|
|__||  ||___||  |_|___|___|__|  ||___||  ||__||_|_|_|_|_|_|_|_|_|_|
||__|  |__|__|  |___|___|___||  |__|__|  |__|||_|_|_|_|_|_|_|_|_|_|
|__||  ||___||  |_|___|___|__|  ||___||  ||__||_|_|_|_|_|_|_|_|_|_|
||__|  |__|__| |     || |     | |__|__|  |__|||_|     Games     |_|
|__||  ||___|| |     || |     | ||___||  ||__||_|.   Consoles   |_|
||__|  |__|__| |     || |     | |__|__|  |__|||_|*`.            |_|
|__||  ||___|| |     || |     | ||___||  ||__||_| S `.          |_|
||__|  |__|__| |     || |     | |__|__|  |__|||_|`. A `.        |_|
|__||  ||___|| |    [|| |]    | ||___||  ||__||_|  `. L `.      |_|
||__|  |__|__| |     || |     | |__|__|  |__|||_|    `. E `.    |_|
|__||  ||___|| |_____|| |     | ||___||  ||__||_|______`__*_`___|_|
||__|  |__|__|_| ____||_|____ | |__|__|  |__|||_|_|_|_|_|_|_|_|_|_|
|***|  |LLLLL|_______________|| |LLLLL|  |LLL|  |LLLLL|LLLLL|LLLLL|
|***|  |LLL|________________| | |LLLLL|  |LLL|  |LLLLL|LLLLL|LLLLL|
|***|__|L|_________________|__|_|LLLLL|__|LLL|  |LLLLL|LLLLL|LLLLL|
'''

    print(figure)

def show_inside():
    entrance = """

|.'',                                                  ,''.|
|.'.'',                                              ,''.'.|
|.'.'.'',                                          ,''.'.'.|
|.'.'.'.'',                                      ,''.'.'.'.|
|.'.'.'.'.|              __                      |.'.'.'.'.|
|.'.'.'.'.|===;        G|00|P                ;===|.'.'.'.'.|
|.'.'.'.'.|:::|',       \==/  #            ,'|:: |.'.'.'.'.|
|.'.'.'.'.|---|'.|,    ||  |==|           |.'|---|.'.'.'.'.|
|.'.'.'.'.|:::|'.|'|___||__|_____         |.'|:: |.'.'.'.'.|
|,',',',',|---|',|'|            |         |,'|---|,',',',',|
|.'.'.'.'.|:::|'.|'|____________|         |.'|:: |.'.'.'.'.|
|.'.'.'.'.|---|','   /%%%\                ','|---|.'.'.'.'.|
|.'.'.'.'.|===:'    /%%%%%\                 ':===|.'.'.'.'.|
|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
|.'.'.'.','       /%%%%%%%%%\                    ','.'.'.'.|
|.'.'.','        /%%%%%%%%%%%\                     ','.'.'.|
|.'.','         /%%%%%%%%%%%%%\                      ','.'.|
|.','          /%%%%%%%%%%%%%%%\                       ','.|
|;____________/%%%%%%%%%%%%%%%%%\             ____________;|

"""
    print("ENTERING STORE...\n\n")
    time.sleep(2)
    print(entrance)

def show_game_display():
    # Do not change 75 below, it is needed for correct image.
    game_display = '''

 ,.,||-------------------------------------------------------||,., ,.,
 ,.,||-------------------------------------------------------||,., ,.,
 ,.,||                                                       ||,., ,.,
 ,.,||    _________    _________    _________    _________   ||,., ,.,
 ,.,||   |         |  |         |  |         |  |         |  ||,., ,., 
 ,.,||   |   HALO  |  | RAINBOW |  |  GEARS  |  |  Call   |  ||,., ,.,
 ,.,||   |         |  |    6    |  |   OF    |  |   of    |  ||,., ,.,
 ,.,||   |         |  |  SIEGE  |  |   WAR   |  |  DUTY   |  ||,., ,.,
 ,.,||   |         |  |         |  |         |  |         |  ||,., ,.,
 ,.,||-------------------------------------------------------||,., ,.,
 ,.,||---SHOOTERS--------------------------------------------||,., ,.,
 ,.,||-------------------------------------------------------||,., ,.,
 ,.,||                                                       ||,., ,.,
 ,.,||                                                       ||,., ,.,
 ,.,||    _________    _________    _________    _________   ||,., ,.,
 ,.,||   |         |  |         |  |         |  |         |  ||,., ,.,
 ,.,||   |  ZELDA  |  |  FINAL  |  |  ZELDA  |  |  ELDEN  |  ||,., ,.,
 ,.,||   |         |  | FANTASY |  |         |  |   RING  |  ||,., ,.,
 ,.,||   |         |  |  *****  |  |         |  |         |  ||,., ,.,
 ,.,||   |         |  |  *****  |  |         |  |         |  ||,., ,.,
 ,.,||-------------------------------------------------------||,., ,.,
 ,.,||____RPGs_______________________________________________||,., ,.,
 ,.,||                                                       ||,., ,.,
 ,.,||                                                       ||,., ,.,
 ,.,||   _________    _________    _________     _________   ||,., ,.,
 ,.,||   |        |  |         |  |         |   |         |  ||,., ,.,
 ,.,||   |  2K    |  |  FIFA   |  | MADDEN  |   |   WII   |  ||,., ,.,
 ,.,||   |        |  |         |  |         |   | SPORTS  |  ||,., ,.,
 ,.,||   |        |  |         |  |         |   |         |  ||,., ,.,
 ,.,||   |        |  |         |  |         |   |         |  ||,., ,.,
 ,.,||-------------------------------------------------------||,., ,.,
 ,.,||___SPORTS______________________________________________||,., ,.,

'''
    print(game_display)

def show_cashier(totals=00):

    cashier = f"""
  |____________________________________________________|
  | __     __   ____   ___ ||  ____    ____     _  __  |
  ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |
  ||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |
  ||  |##||  | | || | |JRO|||-|  | |==|+|+||-|-|~||__| |
  ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|
  ||_______________________||__________________________|         ________________________
  | _____________________  ||      __   __  _  __    _ |        |           |            |               
  || | | | | | | | | | | |/\______  |_|  ||#||==|  / / |        |           |            |
  || | | | | | | | | | | (_______ |++|=|  || ||==| / / |        |           |            |
  ||_|_|_|_|_|_|_|_|_|_|_| _  _  |\__|_|__||_||__|/_/__|        |           |            |
  |____________________ /| 0  0   |\ __________________|        |           |            |       
  | __   __    _  _     \_  <     _/                   |        |___________|____________|   
  ||~~|_|..|__| || |_ _   \ ===  /                     |        |           |            |
  ||--|+|^^|==|1||2| | |__|\ __ /|__                   |        |           |            |   
  ||__|_|__|__|_||_|_| /  \______/  \            ______|        |           |            |   
  |_________________ _/              \_ ________|______|        |           |            |
  |                  /       Collin   \|  ___________  |        |___________|____________|
  |                  |___|        |___|| |___{totals}.00__| |
  |                  \  \          /  /|               |
  |___________________\  \________/  /_|               |_____________________________________________/|
  |________________________ ___________|_______________|_____________________________________________|/
  |                                                     ||                                         ||    
  |                                                     ||                                         ||             
  |                                                     ||                                         || 
  |                                                     ||                                         || 
  |                                                     ||                                         ||         
  |                                                     ||                                         || 
  |-----------------------------------------------------||                                         || 
  |_____________________________________________________||                                         || 
    
    """
    print(cashier)
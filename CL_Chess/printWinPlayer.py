WhiteWin = """
                            ██     ██ ██   ██ ██ ████████ ███████     ██     ██ ██  ███    ██ 
                            ██     ██ ██   ██ ██    ██    ██          ██     ██ ██  ████   ██   
                            ██  █  ██ ███████ ██    ██    █████       ██  █  ██ ██  ██ ██  ██    
                            ██ ███ ██ ██   ██ ██    ██    ██          ██ ███ ██ ██  ██  ██ ██    
                             ███ ███  ██   ██ ██    ██    ███████      ███ ███  ██  ██   ████ """
BlackWin = """
                            ██████   ██       █████   ███████ ██  ███   ██     ██ ██  ███    ██
                            ██   ██  ██      ██   ██  ██      ██  ██    ██     ██ ██  ████   ██    
                            ██████   ██      ███████  ██      ████      ██  █  ██ ██  ██ ██  ██ 
                            ██   ██  ██      ██   ██  ██      ██  ██    ██ ███ ██ ██  ██  ██ ██     
                            ██████   ███████ ██   ██  ███████ ██  ███    ███ ███  ██  ██   ████ """
def printWin(turn):
    if(turn=="Black"):
        print(BlackWin)
    else :
        print(WhiteWin)
    print("\n\n\n\n")
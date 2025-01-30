def askUserToGiveInput(turn):
    print(f"\t\t\t\t Its {turn}'s turn")
    print("\t\t\t\t Enter row and colloum num without space eg:'8e' ",end="\n\n")
    f = input("\t\t\t\t From -->  ")
    t = input("\t\t\t\t To  --->  ")
    return [f, t]
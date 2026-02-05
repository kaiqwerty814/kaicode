import random

chooser = random.randint(0,1234)

print(chooser)
terminal_typer = int(input("choose a num between 0 and 1234 "))
 
if chooser != terminal_typer:
    print("GET OUT!!!")

else:
    print("mission complete +respect")



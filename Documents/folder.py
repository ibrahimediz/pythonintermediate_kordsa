import os
liste = os.listdir("Exercises/")
fileName = "03_01_OOPfunds"
for item in liste:
    with open(f"Exercises/{item}/{fileName}.py","a+") as dosya:
        pass
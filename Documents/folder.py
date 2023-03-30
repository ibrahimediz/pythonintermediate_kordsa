import os
liste = os.listdir("Exercises/")
fileName = "02_01_funds"
for item in liste:
    with open(f"Exercises/{item}/{fileName}.py","a+") as dosya:
        pass
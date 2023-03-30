import os
liste = os.listdir("Exercises/")
fileName = "01_01_try_except"
for item in liste:
    with open(f"Exercises/{item}/{fileName}.py","a+") as dosya:
        pass
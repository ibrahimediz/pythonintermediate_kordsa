import os
liste = os.listdir("Exercises/")
fileName = "03____OOPHomework"
for item in liste:
    with open(f"Exercises/{item}/{fileName}.py","a+") as dosya:
        dosya.write("""

# OOP.jpg dosyası içindeki yapıyı dikkate alarak Otomobil classına kadar gelen 
# OOP hiyerarşisini python programlama dili ile yazınız
        """)
import os
liste = os.listdir("Exercises/")
fileName = "03_02_OOPEncaps"
for item in liste:
    with open(f"Exercises/{item}/{fileName}.py","a+") as dosya:
        dosya.write("""
        Bir galeri için tasarlanan bir yazılım içerisinde arabalar bir sınıf üzerinden nesne üretilerek kaydedilmek istenmektedir.
        En az üç örnek özelliği olan (instance attribute ) bir araba sınıfı tasarlayınız
        """)
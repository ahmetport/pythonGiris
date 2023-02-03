import os
from _datetime import datetime
print(os.getcwd()) # C:\Users\gulsah\PycharmProjects\pythonGiris\Os modulu
#os.chdir("C:/Users/user/Desktop") # klasörün yolunu böyle degiştirebiliriz
print(os.listdir())
#os.mkdir("Deneme") # Os modulunun altına dosya oluşturuyor
#os.rmdir("Deneme") # oluşturdugum dosyayı silmek için
#os.makedirs("denem1/deneme2") # iki klasör oluşturur
#os.rmdir("denem1/deneme2") deneme2 sildim
#os.rmdir("denem1")  denem1 sildim
#os.rename("gs.txt","bjk.txt") oluşturdugum dosyanın ismini degiştirdim
print(datetime.fromtimestamp(os.stat("bjk.txt").st_mtime)) # 2022-12-09 10:53:34.272737 degiştirme zamanını verdi



import mouse #Mouse kütüphanesi bu kütüphane sayesinde mouse ile ilgili işlemler rahatlıkla yapabiliriz.
import time #Zaman k.
from colorama import init #Renk kütüphanesi
from colorama import Fore, Back, Style #Renk kütüphanesinin içindeki modüller
init()
print(Fore.CYAN)
print("Mouse Makroya hoşgeldiniz..")
time.sleep(1.4)
süre = int(input("Mouse Makro kaç saniye olsun ---->"))

mouse_hareketleri = [] #Mouse hareketlerini boş bir küme olarak ayarlıyoruz ki önceki kayıtlar sıfırlansın.
mouse.hook(mouse_hareketleri.append) #Mouse u işaretliyoruz böylece onun eylemlerini kayıt altına alıyoruz.
# E kullanıcı sürenin ne kadar kaldığını bilse güzel olur değil mi?

time.sleep(süre/4) #5 saniye boyunca mouse u dinliyoruz(Kayıt alıyoruz/İşaretliyoruz.)
print("Sürenin"+str(süre/4)+"Bitti")
time.sleep(süre/4) #5 saniye boyunca mouse u dinliyoruz(Kayıt alıyoruz/İşaretliyoruz.)
print("Sürenin"+str(süre/2)+"Bitti")
time.sleep(süre/4) #5 saniye boyunca mouse u dinliyoruz(Kayıt alıyoruz/İşaretliyoruz.)
print("Sürenin"+str(süre/3)+"Bitti")
time.sleep(süre/4) #5 saniye boyunca mouse u dinliyoruz(Kayıt alıyoruz/İşaretliyoruz.)
print("Sürenin"+str(süre/1)+"Bitti")

#Bu kısımları Fonksiyon ilede yazabilirdik ancak şuan da konumuz o değil.
mouse.unhook(mouse_hareketleri.append) #Mouse işaretlemesini bitiriyoruz.
time.sleep(1)
print(Fore.GREEN)
print("Mouse kaydı başlatılıyor.....")
time.sleep(2)
mouse.play(mouse_hareketleri) #İşaretleri/Kayıtları oynatıyoruz.
print("Bizi tercih ettiğiniz için teşekkürler!")
time.sleep(1)
exit()#AlpernT
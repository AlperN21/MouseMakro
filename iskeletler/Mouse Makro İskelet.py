import mouse #Mouse kütüphanesi bu kütüphane sayesinde mouse ile ilgili işlemler rahatlıkla yapabiliriz.
import time #Zaman k.

mouse_hareketleri = [] #Mouse hareketlerini boş bir küme olarak ayarlıyoruz ki önceki kayıtlar sıfırlansın.
mouse.hook(mouse_hareketleri.append) #Mouse u işaretliyoruz böylece onun eylemlerini kayıt altına alıyoruz.

time.sleep(5) #5 saniye boyunca mouse u dinliyoruz(Kayıt alıyoruz/İşaretliyoruz.)

mouse.unhook(mouse_hareketleri.append) #Mouse işaretlemesini bitiriyoruz.
mouse.play(mouse_hareketleri) #İşaretleri/Kayıtları oynatıyoruz.
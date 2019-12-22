import tkinter as tk

def Carpan():
    
    # temel birimler
    girilen = birim1.get()

    if len(girilen) ==2 and (girilen[0] == "G" ):
        carpan1 = 1000000000
    if girilen[0:4] == "ciga":
        carpan1 = 1000000000
    if len(girilen) ==2 and (girilen[0] == "M" ):
        carpan1 = 1000000
    if girilen[0:4] == "mega":
        carpan1 = 1000000
    if len(girilen) ==2 and (girilen[0] == "k" ):
        carpan1 = 1000
    if girilen[0:4] == "kilo":
        carpan1 = 1000
    if len(girilen) ==2 and (girilen[0] == "h" ):
        carpan1 = 100
    if girilen[0:5] == "hekto":
        carpan1 = 100
    if len(girilen) ==3 and (girilen[0:2] == "da" ):
        carpan1 = 10
    if girilen[0:4] == "deka":
        carpan1 = 10
    if len(girilen) ==1 or girilen == "metre" or girilen == "gram" or girilen == "litre" :
        carpan1 = 1
    if len(girilen) ==2 and (girilen[0] == "d"):
        carpan1 = 0.1
    if girilen[0:4] == "desi":
        carpan1 = 0.1
    if len(girilen) ==2 and (girilen[0] == "c"):
        carpan1 = 0.01    
    if girilen[0:5] == "santi":
        carpan1 = 0.01
    if len(girilen) ==2 and (girilen[0] == "m"):
        carpan1 = 0.001
    if girilen[0:4] == "mili":
        carpan1 = 0.001
    if len(girilen) == 2 and (girilen[0] == "u"):
        carpan1 = 0.000001
    if girilen[0:4] == "mikro":
        carpan1 = 0.000001
    if len(girilen) == 2 and (girilen[0] == "n"):
        carpan1 = 0.000000001
    if girilen[0:4] == "nano":
        carpan1 = 0.000000001

        
    istenen = birim2.get()

    if len(istenen) ==2 and (istenen[0] == "G" ):
        carpan2 = 1000000000
    if istenen[0:4] == "ciga":
        carpan2 = 1000000000
    if len(istenen) ==2 and (istenen[0] == "M" ):
        carpan2 = 1000000
    if istenen[0:4] == "mega":
        carpan2 = 1000000
    if len(istenen) ==2 and (istenen[0] == "k" ):
        carpan2 = 1000
    if istenen[0:4] == "kilo":
        carpan2 = 1000
    if len(istenen) ==2 and (istenen[0] == "h"):
        carpan2 = 100
    if istenen[0:5] == "hekto":
        carpan2 = 100
    if len(istenen) ==3 and (istenen[0:2] == "da"):
        carpan2 = 10
    if istenen[0:4] == "deka":
        carpan2 = 10
    if len(istenen) ==1 or istenen =="metre" or istenen =="gram" or istenen =="litre" :
        carpan2 = 1
    if len(istenen) ==2 and (istenen[0] == "d" ):
        carpan2 = 0.1
    if istenen[0:4] == "desi":
        carpan2 = 0.1
    if len(istenen) ==2 and (istenen[0] == "c"):
        carpan2 = 0.01   
    if istenen[0:5] == "santi":
        carpan2 = 0.01
    if len(istenen) ==2 and (istenen[0] == "m"):
        carpan2 = 0.001
    if istenen[0:4] == "mili":
        carpan2 = 0.001

    if len(istenen) == 2 and (istenen[0] == "u"):
        carpan2 = 0.000001
    if istenen[0:5] == "mikro":
        carpan2 = 0.000001
    if len(istenen) == 2 and (istenen[0] == "n"):
        carpan2 = 0.000000001
    if istenen[0:4] == "nano":
        carpan2 = 0.000000001
            
    # diger birimler
    if girilen =="mil":
        carpan1 = 1609.344
    if istenen == "mil":
        carpan2 = 1609.344
        
    if girilen =="inch":
        carpan1 = 0.0254
    if istenen == "inch":
        carpan2 = 0.254
   
    if girilen =="yarda":
        carpan1 = 0.9144
    if istenen == "yarda":
        carpan2 = 0.9144

    if girilen =="fit":
        carpan1 = 0.3048
    if istenen == "fit":
        carpan2 = 0.3048

    if girilen =="angstrom":
        carpan1 = 1.000000000
    if istenen == "angstrom":
        carpan2 = 1.000000000

    if girilen == "deniz mili":
        carpan1 = 1852
    if istenen == "deniz mili":
        carpan2 = 1852

    if girilen =="pika":
        carpan1 = 0.004217396
    if istenen == "pika":
        carpan2 = 0.004217396

    if girilen =="punto":
        carpan1 = 0.00035
    if istenen == "punto":
        carpan2 = 0.00035
        
    if girilen =="ışık yılı":
        carpan1 = 946073047300000
    if istenen == "ışık yılı":
        carpan2 = 946073047300000
         
    if girilen =="ton":
        carpan1 = 1000000
    if istenen == "ton":
        carpan2 = 1000000
        
    if girilen == "carat":
        carpan1 = 0.2
    if istenen == "carat":
        carpan2 = 0.2
        
    if girilen == "pound":
        carpan1 = 453.59237
    if istenen == "pound":
        carpan2 = 453.59237
        
    if girilen == "quintal":
        carpan1 = 100000
    if istenen == "quintal":
        carpan2 = 100000
        
    if girilen =="metreküp":
        carpan1 = 1000
    if istenen == "metreküp":
        carpan2 = 1000
        
    if girilen =="galon":
        carpan1 = 3.78541178
    if istenen == "galon":
        carpan2 = 3.78541178
            
    carpan = carpan1/carpan2
        
    return carpan
    
    
def donustur():
    girdi=giris.get()
    katsayi = Carpan()
    sonuc=float(girdi) * katsayi
    sonucyazı = tk.Label(text=sonuc,fg="blue",width="20",height="2")

    sonucyazı.pack()
    
    
arayuz = tk.Tk()
arayuz.geometry('550x400+400+150')
arayuz.title("birim çevirici 0.0.1")



birimyazi1 = tk.Label(text = "girilen birim",fg="green" )
birimyazi1.pack()
birim1 = tk.Entry(arayuz)
birim1.pack()
birimyazi2 = tk.Label(text = "istenen birim",fg="green" )
birimyazi2.pack()
birim2 = tk.Entry(arayuz)
birim2.pack()
deger = tk.Label(text = "değer",fg="blue" )
deger.pack()
giris = tk.Entry(arayuz)
giris.pack()


düğme = tk.Button(text='dönüştür', command = donustur,fg='red',bg='yellow')
düğme.pack()
arayuz.mainloop()



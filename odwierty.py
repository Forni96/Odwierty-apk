print("Szacowanie strat technologicznych płuczki w odwiercie")
n=1
while True:
    print("numer odwiertu",n)
    n += 1
    print("wprowadz promień odwiertu w metrach")
    r=input()
    r=float(r)
    print("wprowadż głębokość odwiertu w metrach")
    h=input()
    h=float(h)
    print("Na podstawie wzoru na obj w odwiercie 2*o*pi*r*r*h")
    print("zakładamy indywidualne straty dla odwiertu od 0,5 do 2")
    print("przyjmowanym parametrem nich będzie litera o")
    o=input()
    o=float(o)
    if o <= 2:
        v=2*o*3.14*(r**2)*h
        print("twoja objętość straty płuczki wynosi =",v,"m^3")
         print("Teraz obliczenia dotyczące momentów obrotowych płuczki dla danego odwiertu")
        print("wprowadz moment obrotowy dla 300 obr/min")
        M300=input()
        M300=float(M300)
        print("wprowadz moment obrotowy dla 600 obr/min")
        M600=input()
        M600=float(M600)
        print("lepkość plastyczna npl")
        npl=M600-M300
        print(npl,"cP")
        print("lepkość pozorna ns")
        ns=M600/2
        print(ns,"cP")
        print("granica płynięcia Ty")
        Ty=(M300-npl)*0.4788
        print(Ty,"N/m")
    else:
        print("niestety parametr o jest za duży")
        print("powtórz pomiar")
        n -= 1
 
    



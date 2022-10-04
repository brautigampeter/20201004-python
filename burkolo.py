import math

szelesseg=float(input("Szélesség (m): "))
magassag=float(input("Magasság (m): "))

T=(szelesseg*100)*(magassag*100)

Tcsempe=20*20

print(math.ceil((T/Tcsempe)*1.1),"db csempe kell")


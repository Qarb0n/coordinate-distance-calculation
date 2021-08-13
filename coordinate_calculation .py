a = [int(x) for x in input("1. numbers of the first coordinate : ").split("-")]
b = [int(x) for x in input("2. numbers of the second coordinate : ").split("-")]

c =(a[0] - a[1]) ** 2
d =(b[0] - b[1]) ** 2
sonuc = (c + d )** 0.5

print(f"""

Y

|               {d}
|
|
|
|
|   {c}
|       
-----------------------  X

 Distance Between Two Points : {sonuc}


""")
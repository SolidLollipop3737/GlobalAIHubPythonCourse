

x=1
y=2
z=0
print("10 soruluk yarismamiza hos geldiniz!")
print("Sorular tek cevaplidir.")
print("5 soruyu doğru bilirseniz basarili olursunuz.")

while x<y:
  x=x+1
  print ("1. soru: 12'nin karesi kactir?")
  cevap = input("cevabiniz?")
  if cevap == "144":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("2. soru: en koyu renk? ")
  cevap = input("cevabiniz?")
  if cevap == "Siyah":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("3. soru: Türk bayraginda ay yanında ne vardir?")
  cevap = input("cevabiniz?")
  if cevap == "Yildiz":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("4. soru: Türkiyenin en kalabalik sehri ?")
  cevap = input("cevabiniz?")
  if cevap == "Istanbul":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("5. soru: dijital tarih baslangic yili?")
  cevap = input("cevabiniz?")
  if cevap == "1970":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("6. soru: atatürkün 2. adı nedir?")
  cevap = input("cevabiniz?")
  if cevap == "Kemal":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("7. soru: Benim adim nedir?")
  cevap = input("cevabiniz?")
  if cevap == "Onur":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("8. soru: Python mu C++ mı?")
  cevap = input("cevabiniz?")
  if cevap == "Python":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("9. soru: dik üçgenin dik açısı?")
  cevap = input("cevabiniz?")
  if cevap == "90":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1
while x<y:
  x=x+1
  print ("10. soru: Denizlide deniz var mi?")
  cevap = input("cevabiniz?")
  if cevap == "Hayir":
   print("Helal")
   z=z+1
  else:
   print("Yanildin! Harflerin büyük küçük olmasina dikkat et!")
y=y+1

if z < 5:
  print("basarisiz oldunuz")
  print("dogru sayiniz: ", z )
else:
  print("Helal ödülü hak ettin")
  print("dogru sayiniz: ", z )

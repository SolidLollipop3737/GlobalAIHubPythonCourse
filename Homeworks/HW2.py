
cv1={"isim" : "Onur", "soyisim" : "Sever","yas" : "21", "E-mail": "ornek1@hotmail.com", "yetenek": "kodlama"}
cv2={"isim" : "Musa", "soyisim" : "Biyikli","yas" : "18", "E-mail": "ornek2@hotmail.com", "yetenek": "protheus"}
cv3={"isim" : "Furkan", "soyisim" : "akkulak","yas" : "25", "E-mail": "ornek3@hotmail.com", "yetenek": "kodlama"}
cv4={"isim" : "Murat", "soyisim" : "Turker","yas" : "30", "E-mail": "ornek4@hotmail.com", "yetenek": "Blender"}
cv5={"isim" : "Simay", "soyisim" : "Olgac","yas" : "20", "E-mail": "ornek5@hotmail.com", "yetenek": "ingilizce"}
for x in range(6):
  print("^"*20)
  if x == 0:
    print("isim:", cv1["isim"])
    print("soyisim:", cv1["soyisim"])
    print("yas:", cv1["yas"])
    print("E-mail:", cv1["E-mail"])
    print("Yetenek:", cv1["yetenek"])
  elif x == 1:
    print("isim:", cv2["isim"])
    print("soyisim:", cv2["soyisim"])
    print("yas:", cv2["yas"])
    print("E-mail:", cv2["E-mail"])
    print("Yetenek:", cv2["yetenek"])
  elif x == 2:
    print("isim:", cv3["isim"])
    print("soyisim:", cv3["soyisim"])
    print("yas:", cv3["yas"])
    print("E-mail:", cv3["E-mail"])
    print("Yetenek:", cv3["yetenek"])
  elif x == 3: 
    print("isim:", cv4["isim"])
    print("soyisim:", cv4["soyisim"])
    print("yas:", cv4["yas"])
    print("E-mail:", cv4["E-mail"])
    print("Yetenek:", cv4["yetenek"])
  elif x == 4:
    print("isim:", cv5["isim"])
    print("soyisim:", cv5["soyisim"])
    print("yas:", cv5["yas"])
    print("E-mail:", cv5["E-mail"])
    print("Yetenek:", cv5["yetenek"])
  else:
   print("Basvuran sayısı 5'dir!!")






























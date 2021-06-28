
friends =['Doston','Dadajon','O\'ktamjon','Aliyorjon',]
mehmon = friends.append('Boburjon')
mehmon = friends.append('Hamidjon')
mehmon = friends.insert(0,'Valijon') # bunda  insert orqali hohlagan indeksga son va mantn kiitishimiz mumkin

print(friends)
mehmon = friends.remove('Valijon')
mehmon = friends.remove('Hamidjon')
print(friends)
mehmonlar = [] #  bush list

yangi = mehmonlar.append(friends.pop(0))
yangi = mehmonlar.append(friends.pop(1))
yangi = mehmonlar.append(friends.pop(-1))
print(mehmonlar)
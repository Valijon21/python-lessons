
davlatlar = ['Rossia','Uzbekiston','Turkia','Amerika','Germaniya','Angilya']

print(davlatlar)
print(len(davlatlar))
davlatlar.sort()
print(davlatlar) # hariflarni alfabit buyichida tartiblab bereadi
print(sorted(davlatlar)) # bu ham tartiblaydi sorted bu funksiya b-l bunda  avvalgi ruyhatga uzgartirish kiritmaydi
print("sorted funksiya bilan aylantirish:",sorted(davlatlar,reverse=True)) # bunda teskari tartiblaydi

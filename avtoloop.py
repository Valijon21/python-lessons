avtolar = [ 'audi','bmw','honda','hyundai','tico','damas']

for avto in avtolar: # bu yerda avto uzgaruvchisiga avtolar siklini 
    if avto == 'bmw': # agar avto uzgaruvhisi bmw nomiga kelganda 
        print(avto.upper()) # suzni hammasini katta harifda chiqar
    # yuqorida gi shart bajarilmasa else bajariladi
    else: # aks holda esa 
        print(avto.title())
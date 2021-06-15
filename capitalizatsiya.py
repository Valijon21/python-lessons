# bunda matinni suzlarni bosh harif ga almashtirish chuniladi
a= " piton eng yaxshi dasturlash tillaridan biri hiosblanadi"
print(a.title())  # natija: Piton Eng Yaxshi Dasturlash Tillaridan Biri Hiosblanadi
print(a.lower()) # bu esa hammasini kichik harifda yozish
print(a.upper()) # bu hamasini katta  harifda yozish
# suzni necha baytligini bilish
print(len("matinni necha baytligi biladi".encode('utf-8'))) # bu matn 29 bayt ekan

#  yana harqanday matinni ruyxat qilsih mumkin bunga katta matinlar ham kiradi
b = "valijon"
print(list(b)) # ['v', 'a', 'l', 'i', 'j', 'o', 'n'] shu kurinishda  buladi
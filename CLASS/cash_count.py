a=int(input('enter the num:'))
note_100=0
note_50=0
note_20=0
note_10=0
if a>=100:
    note_100=(a//100)
    a=a%100
if a>=50:
    note_50=(a//50)
    a=a%50
if a>=20:
    note_20=(a//20)
    a=a%20
if a>=10:
    note_10=(a//10)
    a=a%10

print(note_100)
print(note_50)
print(note_20)
print(note_10)


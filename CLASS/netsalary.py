bs=int(input('ENTER THE BASIC SALARY:'))
if bs<5000 :
  da=bs*0.2
  hra=bs*0.25
  pf=bs*0.03
elif bs>=5000 and bs<10000 :
   da=bs*0.17
   pf=bs*0.025
   hra=bs*0.02
elif bs>=10000 and bs<15000 :
  da=bs*0.15
  hra=bs*0.18
  pf=bs*0.02
elif bs>=15000 :
  da=bs*0.12
  hra=bs*0.16
  pf=bs*0.01
ns=bs+da+hra-pf

print("net salary:", ns)
print('da:',da)
print('hra:',hra)
print('pf:',pf)
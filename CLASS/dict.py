cb= {
	'refun' : 94628629987,
	'ringle' : 65874683649,
	'ashik' : 5313658619,
	'akhil' : 65456817424 
}
	
print(cb)
print(' creat new contact means press : 1')
print(' display specifide PH & NAME press :2')
print(' display all PH&NAME press :3')
print(' delete the specifid PH& NAME press :4')
a=int(input('type option :'))
if a==1:
	name =str(input('enter the name : '))
	no=int(input('enter the number:'))
	cb.update({name : no})
	print('update contact is:')
	print(cb)
elif a==2:
	name =str(input('enter the name : '))
	print(cb[name])
elif a==3:
	print(cb)
elif a==4:
	name =str(input('enter the deleting  name : '))
	cb.pop(name)
	print(cb)
	

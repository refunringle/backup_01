a=int(input('ENTER THE BASIC MARK1:'))
b=int(input('ENTER THE BASIC MARK2:'))
c=int(input('ENTER THE BASIC MARK3:'))

p=(a+b+c)*100/300
if a>=50 and b>=50 and c>=50:
 if p>=90:
  print('student grade is a+ with',p,'%') 
 elif p>=90 and p<80:
   print('student grade is a with',p,'%') 
 elif p>=80 and p<75:
  print('student grade is b+ with',p,'%') 
 elif p>=70 and p<75:
  print('student grade is b with',p,'%')  
 elif p>=70 and p<60:
  print('student grade is c+ with',p,'%')
 elif p>=60 and p<50:
  print('student grade is c with',p,'%')  
else:
 print('student is failed!')

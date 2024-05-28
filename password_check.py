a,b,c,d=0,0,0,0
password=input("Enter  your password:-")
caps=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
small=("abcdefghijklmnopqrstuvwxyz")
special=("!@#$%^&*()_+~")
digits=("1234567890")
if (len(password)>=8):
     for i in password:
         if ( i in caps):
             a+=1
         elif ( i in small):
             b+=1
         elif ( i in special):
             c+=1
         elif (i in digits):
             d+=1
              
if( a>=1 and b>=1 and c>=1 and d>=1 and a+b+c+d== len(password)):
    print("valid password")
    print("caps:-",a)
    print("small:-",b)
    print("special:-",c)
    print("digts:-",d)
else:
    print("invalid password")
    print("caps:-",a)
    print("small:-",b)
    print("special:-",c)
    print("digts:-",d)
    
              
    
     

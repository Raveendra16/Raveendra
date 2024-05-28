from tkinter import *
import random
root=Tk()
root.geometry("1000x500")
root.title("dice game")
root.resizable(False,False)


def roll():
 x=random.randrange(1,7)
 global result
 if x==1:
     result="""
     
  o  
     


 """
 
 elif x==2:
     result="""

     
 o o 
     
"""
 elif x==3:
     result="""

  o  
  o  
  o  
"""
 elif x==4:
     result="""

 o o 
      
 o o 
"""
 elif x==5:
     result="""

 o   o 
   o   
 o   o
"""
 elif x==6:
     result="""

o o o
     
o o o
"""

 resultLabel.config(text=result)

#it is 2frame
def press():
 x=random.randrange(1,7)
 global result
 if x==1:
     result="""
     
  o  
     


 """
 
 elif x==2:
     result="""

     
 o o 
     
"""
 elif x==3:
     result="""

  o  
  o  
  o  
"""
 elif x==4:
     result="""

 o o 
      
 o o 
"""
 elif x==5:
     result="""

 o   o 
   o   
 o   o
"""
 elif x==6:
     result="""

o o o
     
o o o
"""
 resultLabel1.config(text=result)
 exit()

#heading
Label(text="DICE GAME",fg="red",font=("Calibri",33),width="300",height="2").pack()

#Frame1

f=Frame(root,bg="red",bd=5,highlightbackground="black",highlightthickness=1,width=310,height=370)
f.place(x=10,y=118)

btn_total=Button(f,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="PRESS",command=roll)
#output
resultLabel=Label(f,text='',font=90,bg='green',fg='white',width=20,height=10)
resultLabel.place(x=40,y=50)




btn_total.place(x=75,y=300)

lbl_out=Label(f,font=("aria",20,'bold'),text="A",width=16,fg="lightyellow",bg="red")
lbl_out.place(x=5,y=30)


#Frame2

f1=Frame(root,bg="lightgreen",bd=5,highlightbackground="black",highlightthickness=1,height=370,width=300)
f1.pack()

#Frame3
f2=Frame(root,bg="green",highlightbackground="black",highlightthickness=3,width=300,height=370)




f2.place(x=690,y=118)

btn_press=Button(f2,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="PRESS",command=press)
btn_press.place(x=75,y=300)
#output
resultLabel1=Label(f2,text='',font=40,bg='red',fg='white',width=20,height=10)
resultLabel1.place(x=40,y=50)

lbl_out=Label(f2,font=("aria",20,'bold'),text="B",width=16,fg="lightyellow",bg="green")
lbl_out.place(x=5,y=30)
mainloop()

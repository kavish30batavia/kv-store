from tkinter import*
import re
       


  
    
def i0():
   
    a=open("a.txt",'r')
    random=0
    count1=0
    x=0
    value=0
  
    for i in a:
        for j in i:
            if j.isdigit()==True:
              
                if random<int(j):
                    random=int(j)
                    x=random
 

    
    return x               
def i1():
    
    a=open("a.txt",'r')
    random=i0()
    count1=0
    x=0
    value=0
    for k in a:
         for l in k:
            
            
            if l==str(random):
                count1=count1+1
                
                 
                if count1==2:
                    value=1
                    x=random+1
                else:
                    x=random
    
    return x

def count11():
    a=open("a.txt",'r')
    random=i1()
    count1=0
    x=0
    value=0
    for k in a:
         for l in k:
            
            
            if l==str(random):
                count1=count1+1
                
                 
                if count1==1:
                    
                    x=1
                else:
                    x=0
    
    return x

i=i1()

count=count11()
def set1():
    
     global i
     global count 
     t1=textbox1.get()
     t2=textbox2.get()
     
      
     if count<1:
              count=count+1
              print(i)
              a=open(f"a{i}.txt",'a')
              a.writelines(t1)
              a.writelines(":")
              a.writelines(t2)
              a.writelines("\n")
              b=i
              
          
          
     else:
         
           
          count=0
          a=open(f"a{i}.txt",'a')
          print(i)
          a.writelines(t1)
          a.writelines(":")
          a.writelines(t2)
          a.writelines("\n")
          b=i 
          i=i+1
     d = open('a.txt', 'a')
     d.writelines(t1)
     d.writelines(":")
   
  
     d.writelines(str(b))
     d.writelines("\n")
     d.close()
 
          
z=-1       
def get():
   global z
   value=0
   t1=textbox1.get() 
   a=open("a.txt",'r')
   for i in a:
       z=z+1
       for j in i:
         if value==1:
               break
      
         if t1==j:
              
               if z%2==0:
                   y=int(z/2)
                   return y
                   
                   z=-1
                   value=1
                   break
               else:
                   y=z+1
                   y=int(z/2)
                   return y
                   z=-1
def get1():
    value=0
    getfile=get()
    t1=textbox1.get() 
    a=open(f"a{getfile}.txt",'r')
    for i in a:
       
       for j in i:
         if value==1:
               break
         
      
         if t1==j:
             print(i)
             value=1
             break
    
    
       
root=Tk()
root.geometry('300x400')
label1=Label(root,text="key").grid(row=1,column=1)
textbox1=Entry(root)
textbox1.grid(row=1,column=2)
label2=Label(root,text="value").grid(row=2,column=1)
textbox2=Entry(root)
textbox2.grid(row=2,column=2)
button1=Button(root,text="set",command=set1)
button1.grid(row=3,column=1)
button2=Button(root,text="get1",command=get1)
button2.grid(row=3,column=2)





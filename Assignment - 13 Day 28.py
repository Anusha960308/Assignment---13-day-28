#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import * 
  
root = Tk() 
root.geometry("300x200") 
  
w = Label(root, text ='GeeksForGeeks', font = "50")  
w.pack() 
  
Checkbutton1 = IntVar()   
Checkbutton2 = IntVar()   
Checkbutton3 = IntVar()


# In[2]:


Button1 = Checkbutton(root, text = "Tutorial",  
                      variable = Checkbutton1, 
                      onvalue = 1, 
                      offvalue = 0, 
                      height = 2, 
                      width = 10)


# In[3]:


Button2 = Checkbutton(root, text = "Student", 
                      variable = Checkbutton2, 
                      onvalue = 1, 
                      offvalue = 0, 
                      height = 2, 
                      width = 10)


# In[4]:


Button3 = Checkbutton(root, text = "Courses", 
                      variable = Checkbutton3, 
                      onvalue = 1, 
                      offvalue = 0, 
                      height = 2, 
                      width = 10)


# In[ ]:


Button1.pack()   
Button2.pack()   
Button3.pack() 
  
mainloop()


# In[ ]:





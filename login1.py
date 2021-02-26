from tkinter import * 

user_name_data=['xm']
password_data=['9876543210']

def register(entry_username,entery_username,msg):
  if entry_username.get() not in user_name_data:
      user_name_data.append(entry_username.get())
      password_data.append(entry_password.get())
      msg.configure(text="Registered successfully")
      print(entry_username.get(),"      ",entry_password.get())
  else:
      msg.configure(text="Failed to register...")

def reg():
  win-Tk()
  win.title("Registration window")
  username=Label(win,text="USERNAME: ") 
  entry_username=Entry(win)  
  password=Label(win,text="PASSWORD :")  
  entry_password=Label(win,show="*")
  msg=Label(win)  
  register_button=Button(win,text="Register", command=lambda:register(entry_username,entry_password,msg)   

def login(entry_username,entry_password,msg):
  if entry_username.get() in user_name_data :
    if password_data[user_name_data.index(entry_username.get()]==entry_password.get(): 
        msg.configure(text="Login Successful!")
    else:
      msg.configure(text="Login Failed!")
  else:
    msg.configure(text="User does not exist. Please register as new user.")

def ui ():
  root=Tk()
  root.title('Login UI')
  heading=Label(ROOT,TEXT="Login UI", font=40)

  username=Label(root, text="USERNAME:")  
  entry_username=Entry(root,show='*')
  entry_password=Entry(root,text="Login",command=lambda:login(entry_username,entry_password,msg))
  login_button=Button(root,text="Register",command=lambda:reg())
  msg=Label(root)

#grid
  heading.grid(row=0,columnspan=2)
  username.grid(row=1,column=0)
  entry_username.grid(row=1,column=1)

  password.grid(row=2,column=0)
  entry_password.grid(row=2,column=1)

  login_button.grid(row=3,columnspan=2)
  register_button.grid(row=4,columnspan=2)
  msg.grid(row=5,columnspan=2)
  print("USERNAME             PASSWORD")
  print("================================")
  print(user_name_data[0],"         ",password_data[0])
  mainLoop()

if __name___=='__main__':
  ui()
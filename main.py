users = {}
status = ""

def displayMenu():
  status = input("Registered user? y/n? Press q to quit. ");

  if status == "y":
    oldUser()
  elif status == "n":
    newUser()

def newUser():
    createLogin = input("\nCreate login username: ")

    if createLogin in users:
      print("\nLogin name already exists!\n")
    else: 
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        print("\nUser created\n")
def oldUser():
  login = input("Enter login name: ")
  passw = input("Enter password: ")

  if login in users and users[login] == passw:
      print("\nLogin successful!\n")
  else:
      print("\nUser does not exist or incorrect password!\n")

while status != "q":
    displayMenu()
    

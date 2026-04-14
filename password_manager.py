pwd=input("Enter the Master Password: ")

def view():
    with open('password.txt','r') as f:
        # running a for loop on each line and using f.readlines to read them individually
        for line in f.readlines():
            # removing the character return or next line \n effect
            print(line.rstrip())
def add():
    name=input("Enter your Full name: ")
    password=input("Enter your password: ")
    with open('password.txt','a') as f:
        f.write(name+"|"+password+"\n")

if pwd=='Master':
    mode=input("Do you want to add, view passwords or press q to quit: ")
    if mode.lower()=="view":
        view()
    elif mode.lower()=="add":
        add()
    elif mode.lower()=="q":
        quit()
    else:
        print("Invalid Selection.")
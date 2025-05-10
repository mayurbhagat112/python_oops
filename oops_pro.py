import getpass

class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggin=False
        self.menu()
    
    def menu(self):
        user_input=input("""welcome to chatbook !! how would you like to procced
                        1. press 1 to singup
                        2. press 2 to signin
                        3. press 3 to write a post
                        4. press 4 to message a friend
                        5. press any other key to exit""")
        if user_input=="1":
            self.singup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()

    def singup(self):
        email=input("enter the email here ->")
        password = getpass.getpass("Enter your password: ")
        self.username=email
        self.password=password
        print("you have sing up succefully")
        print("\n")
        self.menu()


    def signin(self):
        if self.username=="" and self.password=="":
            print("please signup first pressing 1")
        else:
            uname=input("enter your email/username here ->")
            pwd=getpass.getpass("Enter your password: ")
            if uname==self.username and pwd==self.password:
                print("you have logged in succefully")
                self.loggin=True
            else:
                print("please input correct crdentail")
            print("\n")
            self.menu()

obj=chatbook()
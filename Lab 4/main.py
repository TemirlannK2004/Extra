
class UserForm:
    def __init__(self):
        self.data = {}
        self.users_list=[]
        self.not_auth = 'Authorization'
        self.flag = True

    def options_message(self):
        
        print("Choose an option:")
        print("1. Create User")
        print("2. Show List of Users")
        print("3. Delete User from List")
        print(f"4. {self.not_auth}")
        print("5. Exit")


    def create_user(self):
    
            self.data['Name'] = str(input('Enter Name:'))
            self.data['Surname']=str(input('Enter Surname:'))
            self.data['Age'] = int(input('Enter Age:'))
            self.data['Email'] = str(input('Enter Email:'))
            self.data['Password'] = str(input('Enter Password: '))
            if any(user['Email'] == self.data['Email'] for user in self.users_list):
                print('Email should be unique')
                return
            if len(self.data['Password'])<8:
                print('Password must be at least 8 characters long.')
                return
            else:
                self.users_list.append(self.data.copy())
                print('User Created!')


    def show_users_list(self):
        for user in self.users_list:
            print(f"""
        Name:{user['Name']}
        Surname:{user['Surname']}
        Age:{user['Age']}
        Email:{user['Email']}
                """)  

    
    def delete_user(self):
        pick_user_email = str(input('Enter email:'))
        for user in self.users_list:
            if pick_user_email == user['Email']:
                self.users_list.remove(user)
                print(f"User with email  {pick_user_email} deleted")
                return 
        print('Error 404-Not found')
            


    def user_authorization(self):
        
        while True:
            if self.flag == True:
                email = str(input('Enter Email:'))
                password = str(input('Enter Password:'))
                for user in self.users_list:
                    if email==user['Email'] and password==user['Password']:
                        print('You Successfully logged in to the System!')
                        print(f"Hello,{user['Name']}")
                        self.not_auth = 'Logout'
                        self.flag = False
                        return
                print('Wrong Email or Password, Try Again')
            else:
                self.not_auth = 'Authorization'
                print('Logged Out!')
                return

    def run(self):
        self.options_message()

        choice = int(input('Please write correct number: '))

        if choice == 5:
            return False

        if choice == 1:
            self.create_user()
        if choice == 2:
            self.show_users_list()     

        if choice ==3:
            self.delete_user()

        if choice==4:
            self.user_authorization()
        else:
            print('Enter coorect number')


user_form=UserForm()
while True:
    if user_form.run() == False :
        print('Bye!See you later!')
        break



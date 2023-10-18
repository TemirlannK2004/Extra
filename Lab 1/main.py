class Form:
    def __init__(self):
        self.data = {}

    def welcome_message(self):
        print("Welcome dear user, you can fill this form!")
    def bye_message(self):
        print("Thank you for your time, have a nice day!")


    def fill_name(self):
        self.data['Name'] = str(input("Enter your Name: "))
        self.data['Surname'] = input("Enter your Surname: ")


    def fill_birth_year(self):
        try:
            birth_year = int(input("Enter your date of birth: "))
            self.data['Birth_Year'] = birth_year
        except ValueError:
            print('Birth_Year should be integer')


    def fill_additional_questions(self):
        self.data['City'] = input("In which town you live? - ")
        self.data['University'] = input("What university do you study at? -")


    def display_data(self):
        print('')
        print(f"User info:")
        for key, value in self.data.items():
            print(f"{key}: {value}")


    def run(self):
        self.welcome_message()
        self.fill_name()
        self.fill_birth_year()
        self.fill_additional_questions()
        self.display_data()
        self.bye_message()

if __name__ == "__main__":
    form = Form()
    form.run()
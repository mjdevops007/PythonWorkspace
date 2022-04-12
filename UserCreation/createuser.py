class User():
    def __init__(self, name, email, password, address):
        self.name = name;
        self.email = email;
        self.password = password;
        self.address = address;

    def update_password(self, pwd):
        self.password = pwd
        print("Password updated succesfully ")

    def update_address(self, add):
        self.address = add
        print("address updated succesfully ")

    def get_user_details(self):
        print(f"user is {self.name}")
        print(f"email is {self.email}")
        print(f"address is {self.address}")
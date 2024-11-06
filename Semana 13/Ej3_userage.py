from datetime import date

class User:
    email: str
    password: str
    date_of_birth: date

    def __init__(self,email,password,date_of_birth ):
        self.email = email
        self.password = password
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )
    
def check_user_age(func):
    def wrapper(user: User, *args, **kwargs):
        if user.age < 18:
            raise ValueError("User must be at least 18 years old.")
        return func(user, *args, **kwargs)
    return wrapper

@check_user_age
def access_restricted_area(user: User):
    return ("Access granted to restricted area")

user1 = User("robtoto@gmail.com", "ultrasecurepassword", date(1999, 8, 12))
user2 = User("mariappp@gmail.com", "secretsecpassword", date(2010, 5, 20))

try:
    print(access_restricted_area(user1))
except ValueError as e:
    print("Error:", e)

try:
    print(access_restricted_area(user2))
except ValueError as e:
    print("Error:", e)
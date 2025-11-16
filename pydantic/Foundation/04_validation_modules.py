# ✔ field_validator
# -> A function that validates or modifies a single field before storing it.

#  Example: Let’s validate that age must be >= 18.

from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    name: str
    age: int

    @field_validator("age")
    def age_must_be_valid(cls, value):
        if value < 18:
            raise ValueError("You must be 18+ to enter!")
        return value


user = User(name="Asad", age=20)
print(user)
# [NOTE]: If someone enters age = 10
# -> OUTPUT:- ValueError: You must be 18+ to enter!


# ✔ model_validator
# -> A function that validates or modifies the entire model, using all fields together.
# Example: password and confirm_password match
class Signup(BaseModel):
    username: str
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match!")
        return self

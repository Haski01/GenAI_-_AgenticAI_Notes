from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str
    is_active: bool


user = User(name="Asad", age="22", email="asad@example.com", is_active=True)

# Wrong Data (Error Example)
# user = User(name=123, age="hello", email="asad@example.com")

print(user)

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address


address = Address(street="123 something", city="Meerut", postal_code="250001")

user = User(
    id=1,
    name="Asad",
    address=address,
)

user_data = {
    "id": 1,
    "name": "Hitesh",
    "address": {"street": "321 something", "city": "Paris", "postal_code": "20002"},
}

user = User(**user_data)
print(user)

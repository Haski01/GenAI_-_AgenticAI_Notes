from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


input_data = {
    "id": 100,
    "name": "Asad",
    "price": "400.00",
}

p1 = Product(**input_data)  # "**" means to un-pack data OR spread data

product_one = Product(id=1, name="Laptop", price=999.99, in_stock=True)
product_two = Product(id=2, name="Mouse", price=24.33)
product_three = Product(name="keyboard")

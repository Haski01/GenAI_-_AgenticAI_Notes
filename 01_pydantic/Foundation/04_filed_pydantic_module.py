# Pydantic’s Field() is used to add validation rules, metadata, default values, constraints, and documentation to individual fields inside a Pydantic model.

from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    name: str = Field(default="Unknown")
    age: int = Field(..., ge=18, description="Must be 18 or older")


"""
✔ Explanation:
- default="Unknown" → default value if user doesn’t provide name
- ... → required field
- ge=18 → age >= 18
- Description added for documentation
"""


class Product(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)
    quantity: int = Field(default=1, ge=0)


"""
✔ What this means:
   - title must be between 3 to 50 characters
   - price must be greater than 0
   - quantity must be >= 0, default is 1
"""


# Another exaple.
class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Mohammad Asad",
    )
    department: Optional[str] = "General"
    salary: float = Field(..., ge=10000)

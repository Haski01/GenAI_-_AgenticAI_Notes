from typing import Optional
from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Hitesh Choudhary",
    )
    department: Optional[str] = "General"
    salary: float = Field(..., ge=10000)


employee_data = {"id": 101, "name": "Irtika Ansari", "salary": 100000}

emp1 = Employee(**employee_data)
print(emp1)

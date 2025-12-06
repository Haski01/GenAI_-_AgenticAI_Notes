# computed_field is a Pydantic decorator used to create read-only fields whose values are automatically calculated from other fields in the model.

# EXAMPLE 1 — BMI Calculator

from pydantic import BaseModel, computed_field, Field


class Person(BaseModel):
    name: str
    height: float  # in meters
    weight: float  # in kg

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height**2)
        # return bmi:.2f


p = Person(name="Asad", height=1.75, weight=70)
# print(p.bmi)


# EXAMPLE 2 - Room booking
class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night


booking = Booking(user_id=123, room_id=456, nights=3, rate_per_night=100.0)

print(booking.total_amount)
print(booking.model_dump())

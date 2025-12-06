# serialization: Converting Pydantic models → dict/JSON/string.
# model_dump(): Gives Python dictionary, No formatting applied.
# model_dump_json(): Gives JSON string, Uses json_encoders for formatting.
# ConfigDict(json_encoders): Customizes how data types (like datetime) appear in JSON.


from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Event(BaseModel):
    title: str
    time: datetime

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%Y-%m-%d %H:%M")}
    )


event = Event(title="AI Workshop", time=datetime.now())

print(event.model_dump())  # Python dict
print(event.model_dump_json())  # JSON string with custom date format

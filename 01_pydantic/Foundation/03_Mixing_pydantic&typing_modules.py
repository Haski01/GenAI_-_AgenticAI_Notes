from pydantic import BaseModel
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None


cart_data = {
    "user_id": 123,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "quantities": {"laptop": 1, "mouse": 2, "keyboard": 3},
}

blog_data = {
    "title": "This is my first blog",
    "content": "About my life best movements",
}

cart = Cart(**cart_data)
blog = BlogPost(**blog_data)
print(cart)
print(blog)

from datetime import date
from pydantic import BaseModel, Field, field_validator, EmailStr
from enum import Enum
from typing import List, Optional


class User(BaseModel):
    fio: str = Field(max_length=50, min_length=3)
    age: int = Field(ge=1, le=100)

    @field_validator('fio')
    @classmethod
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('Имя должно иметь пробел')
        return v

class Major(str, Enum):
    informatics = "Информатика"
    economics = "Экономика"
    law = "Право"
    medicine = "Медицина"

class Student(BaseModel):
    first_name: str
    major: Major = Field(description="Специальность студента")

class Category(str, Enum):
    electronics = "Электроника"
    clothing = "Одежда"
    books = "Книги"
    home = "Домашние товары"

class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)
    tags: Optional[List[str]] = Field(default_factory=list)
    category: Category = Field(description="Категория товара")
    description: Optional[str] = None
    in_stock: bool = True


class OrderItem(BaseModel):
    item_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0)


class Order(BaseModel):
    order_id: int = Field(..., description="Идентификатор заказа")
    items: List[OrderItem] = Field(..., min_length=1, description="Список позиций заказа")
    customer_email: EmailStr = Field(..., description="Email покупателя")
    delivery_date: date = Field(..., description="Дата доставки")

    @field_validator("delivery_date")
    @classmethod
    def delivery_date_not_past(cls, v: date) -> date:
        if v < date.today():
            raise ValueError("Дата доставки не может быть в прошлом")
        return v

from fastapi import FastAPI
from day3.models import User, Student, Product, Order


app = FastAPI()

users = {}
products = {}
orders = {}

@app.post("/users")
async def create_user(user: User):
    user_id = len(users) + 1
    users[user_id] = user.model_dump()
    return users[user_id]

@app.get("/users")
async def get_users():
    return users

@app.post("/student")
async def create_student(st: Student):
    return st



@app.get("/products")
async def get_products():
    return products


@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return products.get(product_id, {"error": "not found"})


@app.post("/products")
async def create_product(product: Product):
    product_id = len(products) + 1
    products[product_id] = product.model_dump()
    products[product_id]["id"] = product_id
    return products[product_id]


@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    products[product_id] = product.model_dump()
    products[product_id]["id"] = product_id
    return products[product_id]


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    if product_id in products:
        del products[product_id]
        return {"ok": True}
    return {"error": "not found"}



@app.get("/orders")
async def get_orders():
    return orders


@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    return orders.get(order_id, {"error": "not found"})


@app.post("/orders")
async def create_order(order: Order):
    orders[order.order_id] = order.model_dump()
    return orders[order.order_id]


@app.put("/orders/{order_id}")
async def update_order(order_id: int, order: Order):
    orders[order_id] = order.model_dump()
    return orders[order_id]


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    if order_id in orders:
        del orders[order_id]
        return {"ok": True}
    return {"error": "not found"}
























# items = {}


# class Book(BaseModel):
#     title: str
#     author: str
#     year: int

# @app.get("/items/{item_id}")
# async def get_item(item_id: int):
#     return items.get(item_id, {"error": "not found"})


# @app.post("/items")
# async def create_item(name: str, price: float):
#     item_id = len(items) + 1
#     items[item_id] = {"id": item_id, "name": name, "price": price}
#     return items[item_id]

# @app.post("/books")
# async def create_book(book: Book):
#     return book


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, name: str, price: float):
#     items[item_id] = {"id": item_id, "name": name, "price": price}
#     return items[item_id]


# @app.delete("/items/{item_id}")
# async def delete_item(item_id: int):
#     if item_id in items:
#         del items[item_id]
#         return {"ok": True}
#     return {"error": "not found"}

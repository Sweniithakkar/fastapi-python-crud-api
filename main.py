from fastapi import FastAPI
from models import Product
from database import sessionlocal as sesion,engine
import database_models

app = FastAPI()
database_models.base.metadata.create_all(bind=engine)
@app.get("/")
def greet():
    return "Welcome to telusco world"

products =[
    Product(id=1,name="phone",description="smart phone",price=699.99,quantity=50),
    Product(id=2,name="laptop",description="gaming laptop",price=1299.99,quantity=30),
    Product(id=3,name="headphones",description="wireless headphones",price=199.99,quantity=100),
    Product(id=4,name="monitor",description="4K monitor",price=399.99,quantity=20),
    Product(id=5,name="keyboard",description="mechanical keyboard",price=89.99,quantity=75)
]

@app.get("/products")
def get_products():
    db=sesion()
    db.query
    return products

@app.get("/product")
def get_product_by_id():
    return products  # Returns the product with id=3

@app.get("/product/{product_id}")
def get_product_by_id(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"message": "Product not found"}

@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return {"message": "Product added successfully", "product": product}

@app.put("product")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return {"message": "Product updated successfully", "product": updated_product}
    return {"message": "Product not found"}
    
@app.delete("/product")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            del products[index]
            return  "Product deleted successfully"
    return " Product not found"

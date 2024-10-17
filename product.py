# Product 1
product_object_one = {
    "product_id" : 1,
    "product_name" : "Kopiko Black 3 in 1 Twin Pack",
    "product_type" : "Coffee",
    "product_price" : "12.00",
    "product_net_weight" : "60 g",
}
# Product 2
product_object_two = {
    "product_id" : 2,
    "product_name" : "Piattos Sour Cream & Onion",
    "product_type" : "Chips",
    "product_price" : "45.00",
    "product_net_weight" : "85 g"
}
# Product 3
product_object_three = {
    "product_id" : 3,
    "product_name" : "Coke Original",
    "product_type" : "Soft Drink",
    "product_price" : "125.00",
    "product_net_weight" : "1.5 L"
}
# Product 4
product_object_four = {
    "product_id" : 4,
    "product_name" : "Golden Fiesta Cooking Oil",
    "product_type" : "Lipids",
    "product_price" : "72.25",
    "product_net_weight" : "485 ml"
}
# Product 5
product_object_five = {
    "product_id" : 5,
    "product_name" : "Tender Juicy Hotdog Regular",
    "product_type" : "Sausage",
    "product_price" : "226.70",
    "product_net_weight" : "1 kg"
}
# Hold the product dictionaries to products variables
products = [product_object_one,product_object_two,product_object_three,product_object_four,product_object_five]
# Loop through the dictionaries
for product in products:
    # Print the data
    print(f"Product Name: {product.get('product_name')}, Product Type : {product.get('product_type')}, Product Price : {product.get('product_price')}, Product Net Weight : {product.get('product_net_weight')}")

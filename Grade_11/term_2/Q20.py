# Dictionary to store product names and prices
products = {}

# Repeatedly ask the user to enter product names and prices
while True:
    product_name = input("Enter a product name (or 'done' to stop): ")

    if product_name.lower() == 'done':
        break

    try:
        product_price = float(input(f"Enter the price for {product_name}: "))
        products[product_name] = product_price
    except ValueError:
        print("Invalid input. Please enter a valid price.")

# Allow the user to check prices for entered products
while True:
    query_product = input("Enter a product name to check its price (or 'exit' to stop): ")

    if query_product.lower() == 'exit':
        break

    if query_product in products:
        print(f"The price for {query_product} is ${products[query_product]:.2f}")
    else:
        print(f"Product '{query_product}' does not exist.")


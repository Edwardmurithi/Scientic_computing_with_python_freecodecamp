#!/usr/bin/python3

#prompt user to enter products bought by the customer
def store_product_details(product_details, product, price,quantity):
	product_details[product] = [price, quantity]

def totals_for_all_products(product_details):
	# New list to hold cost of each product (price*quantity)
	total_for_each_product = [
		int(value[0]) * int(value[1]) for value in product_details.values()
		]
	return sum(total_for_each_product)

def main():
	# Stores product details
	product_details = {}
	# Prompt User for input
	while True:
		product = input("Product: ")
		if product == 'q':
			break
		price = input("Price: ")
		if price == 'q':
			break
		quantity = input("quantity: ")
		if quantity == 'q':
			break
		store_product_details(product_details, product, price,quantity)

	print(f"TOTALS: {totals_for_all_products(product_details)}")

if __name__ == '__main__':
	main()


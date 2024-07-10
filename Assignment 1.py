#Name: Kavinayan Thayananthakumar            Student Number: 100820472
import time
import random

# Class for product details
class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Category: {self.category}"

# Product management array
class ProductManager:
    def __init__(self):
        self.products = []
        self.id_index = {}
        self.name_index = {}
        self.price_index = {}
        self.category_index = {}

    def load_data_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                id, name, price, category = line.strip().split(',')
                product = Product(int(id), name, float(price), category)
                self.products.append(product)
                self._add_to_indices(product)
        sort_time = self.bubble_sort_by_price() 
        print(f"Data loaded and sorted in {sort_time:.6f} seconds")

    def save_data_to_file(self, filename):
        with open(filename, 'w') as file:
            for product in self.products:
                file.write(f"{product.id},{product.name},{product.price},{product.category}\n")

    def insert_product(self, product):
        self.products.append(product)
        self._add_to_indices(product)
        sort_time = self.bubble_sort_by_price()
        print(f"Product inserted and sorted in {sort_time:.6f} seconds")

    def update_product(self, id, updated_product_info):
        product = self.id_index.get(id)
        if product:
            self._remove_from_indices(product)
            product.name = updated_product_info.get("name", product.name)
            product.price = updated_product_info.get("price", product.price)
            product.category = updated_product_info.get("category", product.category)
            self._add_to_indices(product)
            sort_time = self.bubble_sort_by_price()
            print(f"Product updated and sorted in {sort_time:.6f} seconds")

    def delete_product(self, id):
        product = self.id_index.get(id)
        if product:
            self._remove_from_indices(product)
            self.products.remove(product)
            sort_time = self.bubble_sort_by_price()
            print(f"Product deleted and sorted in {sort_time:.6f} seconds")

    def search_product_by_id(self, id):
        return self.id_index.get(id, None)

    def search_product_by_name(self, product_name):
        return self.name_index.get(product_name.lower().strip(), [])

    def search_product_by_price(self, price):
        return self.price_index.get(price, [])

    def search_product_by_category(self, category):
        return self.category_index.get(category.lower().strip(), [])

    def bubble_sort_by_price(self):
        start_time = time.time()
        n = len(self.products)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.products[j].price > self.products[j+1].price:
                    self.products[j], self.products[j+1] = self.products[j+1], self.products[j]
        end_time = time.time()
        return end_time - start_time

    def _add_to_indices(self, product):
        self.id_index[product.id] = product
        self.name_index.setdefault(product.name.lower().strip(), []).append(product)
        self.price_index.setdefault(product.price, []).append(product)
        self.category_index.setdefault(product.category.lower().strip(), []).append(product)

    def _remove_from_indices(self, product):
        del self.id_index[product.id]
        self.name_index[product.name.lower().strip()].remove(product)
        if not self.name_index[product.name.lower().strip()]:
            del self.name_index[product.name.lower().strip()]
        self.price_index[product.price].remove(product)
        if not self.price_index[product.price]:
            del self.price_index[product.price]
        self.category_index[product.category.lower().strip()].remove(product)
        if not self.category_index[product.category.lower().strip()]:
            del self.category_index[product.category.lower().strip()]

    def print_products(self):
        for product in self.products:
            print(product)

if __name__ == "__main__":
    # Load data from file
    product_manager = ProductManager()
    product_manager.load_data_from_file("product_data.txt")

    # Print initial products
    print("Initial Product List:")
    product_manager.print_products()
    print()

    # Insert a new product
    new_product = Product(57354, "Product E", 29.99, "Category 4")
    product_manager.insert_product(new_product)
    print("After Insertion of Product E:")
    product_manager.print_products()
    print()

    # Update a product
    updated_product = {"name": "Updated Product E", "price": 39.99}
    product_manager.update_product(57354, updated_product)
    print("After Updating Product 57354:")
    product_manager.print_products()
    print()

    # Delete a product
    product_manager.delete_product(57354)
    print("After Deleting Product 57354:")
    product_manager.print_products()
    print()

    # Search for a product by ID
    search_result = product_manager.search_product_by_id(57353)
    print("Search Result for Product with ID 57353:")
    if search_result:
        print(search_result)
    else:
        print("Product not found.")
    print()

    # Search for a product by name
    search_results = product_manager.search_product_by_name("Jacket OTBKQ")
    print("Search Results for Product with Name 'Jacket OTBKQ':")
    if search_results:
        for result in search_results:
            print(result)
    else:
        print("Product not found.")
    print()

    # Search for a product by price
    search_results = product_manager.search_product_by_price(853.38)
    print("Search Results for Products with Price 853.38:")
    if search_results:
        for result in search_results:
            print(result)
    else:
        print("No products found at this price.")
    print()

    # Search for a product by category
    search_results = product_manager.search_product_by_category("Clothing")
    print("Search Results for Products in Category 'Clothing':")
    if search_results:
        for result in search_results:
            print(result)
    else:
        print("No products found in this category.")
    print()

    # Sorting and Complexity Analysis
    random.shuffle(product_manager.products)  # Shuffle list to create a random order
    print("Shuffled Product List:")
    product_manager.print_products()
    print()

    # Bubble Sort and complexity analysis
    bubble_sort_time = product_manager.bubble_sort_by_price()
    print("Bubble Sort Time:", bubble_sort_time)
    print("Sorted List (Bubble Sort):")
    product_manager.print_products()
    print()

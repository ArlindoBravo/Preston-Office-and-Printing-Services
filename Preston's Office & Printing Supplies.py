
def main():
    # Function to Print Catalog
    def prod_list(catalog):
        print("Preston's Printing Catalog")
        for item in catalog:
            print(f"- {item}")

    # Calculation Table
    def calculate_total(sub_total, tax_rate):
        total = sub_total + (sub_total * tax_rate)
        return total

    # Pathway of Choices
    def choice(product, selected_items, Sub_total):
        if product == 'Color Copies':
            Quantity = float(input("How many color copies would you like?: "))
            selected_items.append(product)
            print(f"{product} has been added to your cart.")
            Color_Copy = 0.80
            Sub_total += Color_Copy * Quantity
            
        elif product == 'Black & White Copies':
            Quantity = float(input("How many black & white copies would you like?: "))
            selected_items.append(product)
            print(f"{product} has been added to your cart.")
            BW_Copy = 0.20
            Sub_total += BW_Copy * Quantity
            
        elif product == 'Business Cards':
            print("Our business cards come in two quantity types: \n 50 \n 100 ")
            Draw = str(input("Which quantity type would you like to choose?: "))
            if Draw == "50":
                selected_items.append(product)
                print(f"{product} has been added to your cart.")
                Sub_total += 10.00
            else:
                selected_items.append(product)
                print(f"{product} has been added to your cart.")
                Sub_total += 15.00
                
        elif product == 'Poster':
            selected_items.append(product)
            print(f"{product} has been added to your cart.")
            Sub_total += 20.00
            
        elif product == 'Banner':
            selected_items.append(product)
            print(f"{product} has been added to your cart.")
            Sub_total += 30.00
        return Sub_total 
    
    # Catalog of products the customer chooses
    
    catalog = [
        "Color Copies",
        "Black & White Copies",
        "Business Cards",
        "Poster",
        "Banner"
    ]
    
    # Standard Variables
    
    tax_rate = 0.0825
    Sub_total = 0
    selected_items = []

    # Customer Interaction Start
    
    print("Welcome to Preston's Office & Printing Services!")
    print("My name is Preston!")
    print("It will be my pleasure in attending you today.")
    name = str(input("May I ask to whose name I can put this order for?: "))
    print("Please take a look at our catalog.")
    print()

    prod_list(catalog)

    while True:
        product = input("Please select a product from the catalog (or type 'done' to finish): ").strip()
        print()
        if product.lower() == 'done':
            break
        elif product in catalog:
            Sub_total = choice(product, selected_items, Sub_total) 
        else:
            print("Product not found. Please enter a valid product name.")
    
    if selected_items:
        print()
        print("Receipt:")
        print()
        print("Preston's Office & Printing Services")
        print("----For all your business needs!----")
        print("Cashier: Preston")
        print("Customer: ", name)
        print()
        print("Products Choosen:")
        
        for item in selected_items:
            print(f" - {item}")
        
        # Calculate and display total
        
        total = calculate_total(Sub_total, tax_rate)
        print()
        print(f"Sub_total: {Sub_total:.2f}")
        print(f"Tax: {Sub_total * tax_rate:.2f}")
        print(f"Total: {total:.2f}")
        print()
        print("---Thank you for shoping with us!---")
    else:
        print("No products were selected from our catalog.")

if __name__ == "__main__":
    main()

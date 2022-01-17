from market import GetProduct

if __name__ == "__main__":
    name = input("input name of market product: ")
    name = name.lower()
    product = GetProduct.get_product(name)
    print(product)



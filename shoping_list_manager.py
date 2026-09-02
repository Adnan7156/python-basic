shoping_list = []
while True:
    input_item = input("Add to cart: ")

    if input_item == "done":
        print(f"total item in cart {len(shoping_list)}")
        print(*shoping_list)
        break
    else:
        shoping_list.append(input_item)

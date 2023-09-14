def hello():
    print("hello")

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]


def eat_lunch(food_list):
    if not food_list:
        print("My cookie jar is empty!")
    else:
        print(f"First, I eat a {food_list[0]} cookie")
        for item in food_list[1:]:
            print(f"Next, I eat another {item} cookie")

cookie_items = ["chocolate chip", "oatmeal raisin", "sugar"]


hello()
print(pack)
eat_lunch(cookie_items)
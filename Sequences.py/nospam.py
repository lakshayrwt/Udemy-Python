menu = [
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","spam"],
    ["egg","bacon","spam","sausage"],
    ["spam","bacon","spam","sausage"],
    ["spam","sausage","spam","bacon","spam","tomato","spam"],
    ["egg","bacon","spam","spam","spam","spam"],
]
for meal in menu:
    for index in range(len(meal) -1,-1,-1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)

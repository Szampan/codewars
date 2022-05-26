def dirReduc(arr):
    opposites = [("SOUTH", "NORTH"), ("NORTH", "SOUTH"), ("EAST", "WEST"), ("WEST", "EAST")]
    while True:       
        if not any(pair in [(x, y) for x, y in zip(arr, arr[1:])] for pair in opposites):
            return arr
        for n, item in enumerate(arr[:-1]):
            if (arr[n], arr[n+1]) in opposites:
                arr.pop(n)
                arr.pop(n)
                break
    


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

print(dirReduc(a))
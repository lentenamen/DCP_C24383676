dogs = {"biggie":9}
dogs["lucy"] = 5

for dog,age in dogs.items():
    print(f"{dog}{age}")

for dog in dogs.keys():
    print(f"{dog}:{dogs[dog]}")

for age in dogs.values():
    print(f"{age}")

sorted_dogs = sorted(dogs.items(),key=lambda x: x[1], reverse=True)
items = [10,90,21,45,67,34,12]

search = int(input("search :"))


for x in range(len(items)):
    if(items[x] == search):
        print("found")
        break
    if(search not in items):
        print("not found")
        break

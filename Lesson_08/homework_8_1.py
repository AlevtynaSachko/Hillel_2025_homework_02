def process_list(string_list):
    for item in string_list:
        try:
            numbers = [int(x) for x in item.split(',')]
            print(sum(numbers))
        except ValueError:
            print("Не можу це зробити!")


data = ["5,10,15,555", "33,333,3333,33333,333333", "blablabla,1,2,3"]
process_list(data)
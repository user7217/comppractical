with open('sample1.txt') as f: 
    data = f.read()

def count_char(data, char):
    return len([i for i in data if i ==char])

a = input("enter ")
print(count_char(data, a))
with open("stops.txt", 'r') as f:
    stops_500 = [line.strip() for line in f]
print(stops_500)
stops_final_500 = []
while('' in stops_500):
    stops_500.remove('')
print("updated list:", stops_500)
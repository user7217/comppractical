with open('old.txt', 'r') as old, open('new.txt', 'w') as new:
    new.writelines(line for line in old if not line[0].islower())

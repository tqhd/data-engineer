arr = [10,20,30,50,60,80,110,130]

inp = int(input('Sample input: '))

for index, value in enumerate(arr):
    if value == inp:
        print(f'sample output {index}')
        break
else: 
    print('not found')


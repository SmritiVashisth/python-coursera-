n = 1000
numbers = []
for num in range(2,n):
    numbers.append(num)
    
results = []

while len(numbers)>0:
    number = numbers[0]
    results.append(number)
    remove = []
    for num in numbers:
        if num%number == 0:
            remove.append(num)
    for val in remove:
        numbers.remove(val)
        
print len(results)
    
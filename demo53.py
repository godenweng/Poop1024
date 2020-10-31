numbers = [6,-3,9,-10,4,-7,1,-82,39]


for number in numbers[:]:
    if number < 0:
        numbers.remove(number)
print(numbers)

numbers2 = [6,-3,9,-10,4,-7,1,-82,39]

for n in numbers2[:]:
    if n < 0:
       # numbers2.remove(n)
        numbers2.insert(0,n)
print(numbers2)
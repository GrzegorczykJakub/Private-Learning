cars = ['bwm', 'audi', 'volkswagen', 'ford', 'opel', 'suzuki', 'skoda']

cars.sort()  # sort changes list order forever, not just temporarily
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bwm', 'audi', 'volkswagen', 'ford', 'opel', 'suzuki', 'skoda']
print(cars)

print(sorted(cars))  # sorted sorts list temporarily

cars.reverse() # reverse reverts list permamently
print(cars)
cars.reverse() # using reverse again gets list back to og state
print(cars)

print(len(cars))   # checking lenght of a list using len


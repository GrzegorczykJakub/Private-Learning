guests = ['David', 'Anne', 'Jasmine', 'Alice']
for guest in guests:
    print(guest.title() + ", you are great!")
    print("I really like you " + guest.title() + "\n")
for guest in range(1,3):    #programm stops for loop when it gets to the third item, so the instructions for this item
                            # aren't executed
    print(guest)
for number in range(1, 32, 2): #very useful in numbers genereating(last two tells program to skip elements)
    print(number)
even_numbers = list (range(2, 100, 2)) #generating numbers into list
print(even_numbers)
milion = list (range(1, 1000001))
print(sum(milion))  #adding all numbers from 1 to 1milion

print(guests[1:3])  #using part of the list
for guest in guests[2:]:    #starting on 2 index, looping till the end of a list
    print("These are the guests: "+guest.title())
guests_copy = guests[:] #copying slice of list (whole list)
guests_copy.append('Maria')  #added element will only appear in guests_copy
print(guests_copy)
print(guests)

numbers = (20, 5)   # creating a tuple - similar to lists, but doesn't allow us to change it's items!!! #we use round
                    # brackets instead of square ones
print(numbers)
numbers = (40, 10)  # the only way to change values inside a tuple is to define it again
print(numbers)

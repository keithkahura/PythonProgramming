#my first python list
#numbers = [10,11,34,567,7,3,4,9,76,4,3,2,4]
# print (len (numbers))#get the length of my list)
#for i in range (len (numbers)) :
#print (numbers[i])
#print(numbers.index(76))
#names = ["keith","sam","ivy","grace"]
#print (names.index("grace"))
#append adds a number to a list
#numbers . append(90)
# before appending 
#for i in range (len(numbers)):
    #print (numbers[i])
 
#print ("\n")

#after appending 
#for i  in range (len( numbers)):
    #print(numbers [i])
# element occurs in a list
#print (numbers . count (76)) 
#pop removes an element at a given index
# and returns that element 
#print(numbers.pop(2))

#insert inserts an element (x) ata an index 'y'
# numbers.insert(2, 100)
#remove- removes the first occurence of an element from the list of numbers
#SORT- arranges the list in ascending numbers
# numbers.sort()
# adds a new line for formatted output
# multiplying a list
# zeros = [0]*5
# print(zeros)

# list1 = [23,45]
# list2 = [45,67]
# list3 = list1 +list2
# print(list3)

# print(list3[:1])
#creating empty lists
# nums = []
# for i in range (920):
#  nums.append(i)
even_nums = []
for num in range (20):
    if (num % 2 == 0):
        even_nums.append(num)

# for i in range (len (even_nums)) :
#     print (even_nums[i])

for i in even_nums:
    print(i)    
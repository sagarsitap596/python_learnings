

even_range=range(0,100,2)
odd_range=range(1,100,2)

print(even_range)
print(odd_range)

for i in even_range:
    print(i,end='\t')

print()

for i in odd_range:
    print(i,end='\t')

print()

# creating list from range
odd_list=list(range(1,100,2))
print(odd_list)


original_range=range(100)
half_of_even_range=even_range[2:40:2]
for i in half_of_even_range:
    print(i,end='\t')



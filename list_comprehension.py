a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

even = []

for i in a:
    if i % 2 == 0:
        even.append(i)


print(even)

# list comprehension


new_results = [i for i in a if i % 2 == 0]
print(new_results)

results = [i**2 if i % 2 == 0 else i for i in a]
print(results)

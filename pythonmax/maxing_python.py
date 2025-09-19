# iterar en dos arrays a la vez
heights = [166, 187]
names = ['bob', 'ron']
for h, n in zip(heights, names):
    print(h, n)


#Ordenar un arreglo ascendente
sorted_heights = sorted(heights)
#or
heights.sort()

#DESC
sorted_heights = reversed(sorted(heights))
heights.sort(reverse=True)

# Show only first or lasts rows of array
nums = [2,5,4,2,22,54,21,12]
print(nums[:3]) # [2, 5, 4]
print(nums[5:]) #[54, 21, 12]

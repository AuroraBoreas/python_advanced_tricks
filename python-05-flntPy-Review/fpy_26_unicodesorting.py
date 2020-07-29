import pyuca
coll = pyuca.Collator()
# database
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
# sorting
sorted_fruits = sorted(fruits, key=coll.sort_key)
# display result
print(sorted_fruits)

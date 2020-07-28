import locale
# set up before sorting
locale.setlocale(locale.LC_COLLATE, 'zh_CN.UTF-8')
# database
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
# sorting
sorted_fruits = sorted(fruits, key=locale.strxfrm)
# display result
print(sorted_fruits)

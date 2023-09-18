# list_1 = [1, 2, 3, 4, 5]
# k = 3
# print(list_1.count(k)) 

######################
# list_1 = [1, 2, 3, 4, 5]
# k = 6

# c = []
# for i in list_1:
#     c.append(abs(k-i))
# d = c.index(min(c))
# print(list_1[d])

#########################
k = 'laptop'

points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                count = count + j
print(count)
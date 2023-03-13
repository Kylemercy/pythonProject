# zip  use to combine two or more given iterable
list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'three', 'four', 'five', 'six']
zipped = list(zip(list1, list2))
print(zipped)
# how to unzip
unzipped = list(zip(*zipped))
print(unzipped)
for l1, l2 in zip(list1, list2):
    print(l1, l2)

items = ['egg', 'apple', 'pear', 'tomato', 'potato']
counts = [2, 3, 6, 8, 10]
prices = [0.98, 0.49, 0.23, 0.44, 0.75]
sentences = []
for item, count, price in zip(items, counts, prices):
    sentence = f'i bought {count} {item} for {price} cents'
    sentences.append(sentence)
print(sentences)

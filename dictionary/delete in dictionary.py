# deleting in a dict
# deletion using the pop fun that use abkey
sports = {'peter': 'football', 'john': 'golf', 'ken': 'running', 'dan': 'tennis', 'dil': 'swimming'}
print(sports)
print(sports.pop('peter'))
print(sports)
# using popitem
print(sports.popitem())
# delete any random item in the dict
print(sports)
# using clear or del
del sports['ken']
print(sports)

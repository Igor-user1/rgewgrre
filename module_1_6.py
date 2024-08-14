my_dict = {'name': 'Igor', 'year_of_birth': 1997}
print(my_dict)
print(my_dict['name'])
print(my_dict.get('weight'))


my_dict['phone_number']='+791138414'
my_dict['post_index'] = '555'

p = my_dict.pop('year_of_birth')
print(my_dict)
print(p)
my_set = {1,2,3, 1.5, 'point', True,1,2,3, 1.5, 'point'}
print(my_set)
my_set.add(4)
my_set.add('true')
my_set.remove(1)
print(my_set)

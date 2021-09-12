from create_folders import files, paths, scripts

labels = [
    {'name':'military_ship', 'id':1}, 
    {'name':'speedboat', 'id':2}, 
    {'name':'person', 'id':3}, 
    {'name':'helicopter', 'id':4},
    {'name':'cargo_ship', 'id':5},
    {'name':'fishing_boat', 'id':6},
    ]

with open(scripts['LABELMAP'], 'w') as f:
    for label in labels:
        f.write('item { \n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')
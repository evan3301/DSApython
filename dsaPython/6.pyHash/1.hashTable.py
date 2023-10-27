# TODO: implement a hash table from scratch

'''
Hash tables in python are:
    Implemented via built in dictionary (dict()) type
    Automatically resized
    Accessible via immutable key types (not a list or dict())
'''

hash_person = {'Name': 'Jon' , 'Number': '706-804-4154', 'Adress': '4242 Niche St.'}

# Retrieval
print(hash_person['Name'])

# Replacement
hash_person['Adress'] = '9191 Palace St.'
print(hash_person['Adress'])

# Insertion
hash_person['Disposition'] = 'Scathing'
print(hash_person)

# Deletion
del hash_person['Adress']
print(hash_person)

# Check
if 'Number' in hash_person:
    print('We have a number')

# Time complexity: O(1)
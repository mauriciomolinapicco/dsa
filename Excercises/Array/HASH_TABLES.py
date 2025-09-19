# Creating a dictionary
hash_table = {}

# Inserting key-value pairs
hash_table['apple'] = 10
hash_table['banana'] = 20
hash_table['cherry'] = 30

# Accessing values
print(hash_table['banana'])  # Output: 20

# Deleting an entry
del hash_table['apple']

# Checking existence
if 'cherry' in hash_table:
    print("Cherry exists in hash table")

# Iterating over keys
for key in hash_table:
    print(key, hash_table[key])
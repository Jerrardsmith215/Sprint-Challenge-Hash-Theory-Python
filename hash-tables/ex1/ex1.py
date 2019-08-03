#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length == 1:
        result = None

    # The weight of the item is its key, which decides its index on the table
    # The location of the item is its place in its original array.

    # add items to hashtable
    for location, weight in enumerate(weights):
        hash_table_insert(ht, weight, location)
    
    # TODO
    # return their indexes
    
    # search through values of linked pairs
    for location, weight in enumerate(weights):
        # starting point
        start = weight
        # remainder
        remainder = limit - start
        search = hash_table_retrieve(ht, remainder) # search for remainder
        if search is not None:
            if search > location:
                result = (search, location)
            elif search < location:
                result = (location, search)

    return print_answer(result)

def print_answer(answer):
    if answer is not None:
        print(f'{answer[0]} {answer[1]}')
    else:
        print("None")
#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        hash_table_remove)

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    """
    YOUR CODE HERE
    """
    tix = enumerate(tickets)
    # iterate through tickets and add to hash table

    # build 'blocks' by accessing linked lists

    for index, ticket in tix:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        if ticket.destination is "NONE":
            end = ticket.source  # end
            hash_table_remove(hashtable, ticket.source) # remove end from table
            route[length - 1]

    # set origin and end in route and remove from table
    origin = hash_table_retrieve(hashtable, "NONE")
    route[0], route[length - 1] = origin, "NONE" # set end to 'NONE'

    # proceed from start using queue to fill in blanks
    queue = Queue()
    queue.enqueue(hash_table_retrieve(hashtable, origin))
    hash_table_remove(hashtable, origin) # remove origin from table
    i = 1
    while None in route:
        route[i] = queue.dequeue()
        queue.enqueue(hash_table_retrieve(hashtable, route[i]))
        i += 1

    return(route)
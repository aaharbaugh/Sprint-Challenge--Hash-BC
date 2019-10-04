#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import HashTable


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    for flight in tickets:
        hashtable.hash_table_insert(flight.source, flight.destination)
        if flight.source is 'NONE':
            start = flight.destination

    count = 0

    while start is not None:
        route[count] = start
        start = hashtable.hash_table_retrieve(start)
        count += 1        
        if count >= length:
            start = None


    return route

#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import HashTable


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(42)

    for i, value in enumerate(weights):
        if ht.hash_table_retrieve(limit - value) != None:
            hashtableIndex = ht.hash_table_retrieve(limit - value)
            
            return [i, hashtableIndex]

        ht.hash_table_insert(value, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

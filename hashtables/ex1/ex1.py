#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    answer = None
    for index in range(length):
        weight = weights[index]
        target_weight = limit-weight
        #print(f'Index: {index}; Weight: {weight}; Target: {target_weight}')
        target_index = hash_table_retrieve(ht, target_weight)
        #print(f'Target index: {target_index}')
        if target_index is not None:
            #print('get answer')
            if index > target_index:
                answer = (index, target_index)
            else:
                answer = (target_index, index)
            break
        else:
            #print('Insert value')
            hash_table_insert(ht, weight, index)

    #print('Answer:', answer)
    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

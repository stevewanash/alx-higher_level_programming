#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        list_scores = [a_dictionary[i] for i in a_dictionary]
        key_list = list(a_dictionary)

        return key_list[list_scores.index(max(list_scores))]
    else:
        return None

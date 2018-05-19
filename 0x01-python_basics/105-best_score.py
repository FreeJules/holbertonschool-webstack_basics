#!/usr/bin/python3
def best_score(my_dict):
    if not my_dict:
        return None
    max_score = max(my_dict.values())
    for key, val in my_dict.items():
        if val == max_score:
            return key

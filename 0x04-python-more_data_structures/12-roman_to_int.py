#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = sum((r[roman_string[i]], -r[roman_string[i]])[r[roman_string[i]] < r[roman_string[i+1]]]
                 for i in range(len(roman_string) - 1)) + r[roman_string[-1]]

    return min(max(result, 1), 3999)

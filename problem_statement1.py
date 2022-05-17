import re

OPEN = '('
SQUARE = '['
PARANTHESES = '{'

open_pattern = r"(\(\))"
squae_pattern = r"(\[\])"
parentheses_pattern = r"(\{\})"

def validator(string:str) -> bool:
    is_valid = False
    if OPEN in string:
        is_valid = True if re.search(open_pattern, string) else False
    if SQUARE in string:
        is_valid = True if re.search(squae_pattern, string) else False
    if PARANTHESES in string:
        is_valid = True if re.search(squae_pattern, string) else False
    return is_valid


input1 = '()'
input2 = r'()[]{}'
input3 = '(]'

print(f"""
Input1:
-------
Input: s = \"{input1}\"
Output: {validator(input1)}
-----------------------------
Input2:
-------
Input: s = \"{input2}\"
Output: {validator(input2)}
-----------------------------
Input3:
-------
Input: s = \"{input3}\"
Output: {validator(input3)}
-----------------------------
""")

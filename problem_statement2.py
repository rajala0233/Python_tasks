import re

def validator(a:str, b:str) -> str:
    # Condition to check
    # 1 <= a.length, b.length <= 104
    if (len(a) < 1 or len(a) > 104) or (len(b) < 1 or len(b) > 104):
        raise ValueError('`len(a) or len(b)` should not be less than `1` and greater than `104`.')

    # Condition to check
    # Each string does not contain leading zeros except for the zero itself.
    is_leading_zero = (True if re.search(r'^0*', a) else False) or (True if re.search(r'^0*', b) else False)
    is_zero = (True if re.search(r'^0+[1]+', a) else False) or (True if re.search(r'^0+[1]+', b) else False)

    if is_leading_zero and is_zero:
        raise ValueError('Each string does not contain leading zeros except for the zero itself.')

    # Condition to check
    # a and b consist only of '0' or '1' characters.
    try:
        a = int(a, 2)
        b = int(b, 2)
    except:
        raise ValueError('Please give binary value of `0` or `1`')

    return f"{a+b:b}"

a1 = '11'
b1 = '1'

a2 = '1010'
b2 = '1011'


print(f"""
Input1:
-------
Input: a = \"{a1}\", b = \"{b1}\"
Output: {validator(a1, b1)}
-----------------------------
Input2:
-------
Input: a = \"{a2}\", b = \"{b2}\"
Output: {validator(a2, b2)}
""")

#print("0"*105)

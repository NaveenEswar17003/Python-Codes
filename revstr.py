def rev_str(s):
    rev_str = ''
    for char in s:
        rev_str = char + rev_str
    return rev_str
    
print(rev_str("Hello World"))
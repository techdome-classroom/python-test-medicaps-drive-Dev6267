def isValid(s):
    stack = []
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0

# Test cases
print(isValid("()"))       # Output: True
print(isValid("()[]{}"))   # Output: True
print(isValid("(]"))       # Output: False



  


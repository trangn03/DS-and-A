def reverse_string(input_str):
    # Write your code here
    stack = []
    for char in input_str:
        stack.append(char)
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

original_str = "Hello, World!"
result = reverse_string(original_str)
print(result)  # Output should be "!dlroW ,olleH"

def fibonacci(n):
    if n == 0:  
        return 0
    elif n == 1:  
        return 1
    else:  
        return fibonacci(n - 1) + fibonacci(n - 2)
    

print(fibonacci(6))

def find_subsets(input_set):
    if not input_set:
        return [[]]
    sub=input_set[1:]
    smaller_subsets = find_subsets(sub)
    element = input_set[0]
    subsets_with_element = [subset + [element] for subset in smaller_subsets]
    return smaller_subsets + subsets_with_element

input_set = ['a', 'b', 'c']
subsets = find_subsets(input_set)
print(subsets)
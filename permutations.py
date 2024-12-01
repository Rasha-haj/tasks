def permutations(string):
    result = ['']  

    for char in string:  
        new_result = [] 
        for perm in result:  
            for i in range(len(perm) + 1):  
                new_result.append(perm[:i] + char + perm[i:])
        result = new_result  
    
    return result

result = permutations("abc")
print(result)

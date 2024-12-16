def common_elements_2arrays(arr1,arr2):
    arr2=set(arr2)
    common_elements=[]
    for element in arr1:
        if element in arr2:
            common_elements.append(element)
    return common_elements

#print(common_elements_2arrays([1,2,3,5],[5,2]))


def common_element_3arrays(arr1,arr2,arr3):
    arr2=set(arr2)
    arr3=set(arr3)
    common_elements=[]
    for element in arr1:
        if element in arr2:
            if element in arr3:
             common_elements.append(element)
    return common_elements

#print(common_element_3arrays([1,2,3,5],[5,2],[7]))

def count_vowels_consonants(word):
    word=str(word)
    count_vowels=0
    count_consonants=0
    vowels = "aeiouAEIOU"
    for char in word:
        if char.isalpha():
            if char in vowels:
                count_vowels+=1   
        else:
            count_consonants+=1
    return count_vowels,count_consonants


input="abbdef123"
count_vowels,count_constants=count_vowels_consonants(input)
#print("the count of vowels in" +input+" is:"+str(count_vowels))
#print("the count of constants in" +input+" is:" + str(count_constants))

def find_median_char(word):
    word= str(word)
    just_alpha_chars=[]
    for char in word:
       if char.isalpha()==True:
         just_alpha_chars.append(char)
    
    just_alpha_chars=sorted(just_alpha_chars)
    is_even_len=len(just_alpha_chars)%2
    if is_even_len!=0:
       middle_char= len(just_alpha_chars)//2
       return just_alpha_chars[middle_char]
    else:
        print("there is no median char")

#print(find_median_char("abcdefg"))


import string
def highest_scoring_word(sentance):
    
    sentance=str(sentance)
    arr_words=sentance.lower().split()
    arr_alpha = 'abcdefghijklmnopqrstuvwxyz'
    scores=[]
    
   
    for word in arr_words:
        count_core=0
        for char in word:
            if char.isalpha()==True:
                count_core+= arr_alpha.index(char) + 1
        scores.append(count_core)

    max_scored_num=max(scores)
    index=(scores.index(max_scored_num))
    max_scored_word=arr_words[index]

    return max_scored_word


#print(highest_scoring_word("ab cd ef"))

def return_max_num(num1,num2,num3):
    if num1>num2:
        max_num=num1
    else:
        max_num=num2
    if num3>max_num:
        max_num=num3
    return max_num

print(return_max_num(3,7,5))

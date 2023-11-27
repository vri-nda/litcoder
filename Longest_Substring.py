#  Module 2 - Lab 1 
import sys

def length_of_longest_substring(s):
    #storing the index of the last occurrence of each character
    char_index_map = {}  
    # Starting index of the current substring
    start = 0  
    # Length of the longest substring without repeating characters
    max_length = 0  

    for end in range(len(s)):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            # Move the start pointer to the next index after the repeated character
            start = char_index_map[s[end]] + 1  
            
        # Update the index of the last occurrence of the character
        char_index_map[s[end]] = end  
         # Update the maximum length
        max_length = max(max_length, end - start + 1) 

    return max_length

def doSomething(inval):
    return length_of_longest_substring(inval)

input_val = input()
output_val = doSomething(input_val)
print(output_val)
                                                                                                                            
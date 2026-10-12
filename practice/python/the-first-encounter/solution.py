def first_encounter(s: str) -> dict:
  result = {}
  for index, char in enumerate(s):
    if char not in result:
      result[char] = index
  return result

# Example 1
#print(first_encounter("hello"))  
# Output: {'h': 0, 'e': 1, 'l': 2, 'o': 4}

# Example 2
#print(first_encounter("abc"))    
# Output: {'a': 0, 'b': 1, 'c': 2}

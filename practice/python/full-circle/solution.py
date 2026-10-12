def find_loop_entry(next_indices: list[int])->int:
  visited=set()
  current=0
  n=len(next_indices)
  while 0<=current<n:
    if current in visited:
      return current
    visited.add(current)
    current=next_indices[current]
  return -1
  
  
    
  

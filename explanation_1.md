#Explanation for problem 1: LRU Cache
I used a doubly linked list as a priotity queue to record cache usable and a dictionay for cache items. The doubly linked list will be able to retrieve/update the head (most recently used) element and the tail (least recently used) element with O(1) time. But search will not have a time complexity of O(1). So I incorporated a dictionary to obtain the O(1) time complexity. 


TIME COMPLEXITY - O(1) for get, O(1) for set since items are added at end and pop is done from front(least recently used side)

SPACE COMPLEXITY - O(n) where n is items

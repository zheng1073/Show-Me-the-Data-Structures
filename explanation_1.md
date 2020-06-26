#Explanation for problem 1: LRU Cache
Used doubly linked list with a hash map. Doubly linked list will be able to retrieve/update head (most recently used) element and tail (least recently used) element quite easily. But search it is not O(1). So added in a hash map t speed ip the searching process. 

doubly linked lst as priority queue to record cache usabe and dictionary for cache items


TIME COMPLEXITY - O(1) for get, O(1) for set since items are added at end and pop is done from front(least recently used side)

SPACE COMPLEXITY - O(n) where n is items

#Explanation for problem 1: LRU Cache
Used doubly linked list with a hash map. Doubly linked list will be able to retrieve/update head (most recently used) element and tail (least recently used) element quite easily. But search it is not O(1). So added in a hash map t speed ip the searching process. 

Time and space comlexity --> O(1)

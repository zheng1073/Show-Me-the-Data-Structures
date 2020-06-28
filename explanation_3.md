
The time complexity for the huffman encoding is O(nlog(n)). Iterating through the dataset requires O(n) time but since it also uses 

sorting(which has a time complexity of O(log(n)), the overall time complexity of O(nlog(n)). The time complexity for huffman decoding is 

similar as huffman decoding, except it doesn't need to be sorted, thus it's O(n). The space used is similar to the size of the data thus it's O(n).


The time and space complexities are:
    
    encoding:
       
       time complexity: O(nlog(n)) 
       
       space complexity: O(n)
    
    decoding:
       
       time complexity: O(n) 
       
       space complexity: O(n)


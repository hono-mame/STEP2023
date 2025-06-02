# week2_1.py
* The purpose of this code is to work with a computational complexity of about O(1) by using a hash table.
## Class
* Item
  * |key|: The key of the item. The key must be a string.
  * |value|: The value of the item.
  * |next|: The next item in the linked list. If this is the last item in the linked list, |next| is None.
* HashTable
  * |self.bucket_size|: The bucket size.
  * |self.buckets|: An array of the buckets. self.buckets[hash % self.bucket_size] stores a linked list of items whose hash value is |hash|.
  * |self.item_count|: The total number of items in the hash table.

## Function
* calculate_hash(key)
  * The hash value is obtained by summing the ASCII codes of all characters in the string. This is not the best way to calculate the hash value because it is easy to collide.   
    example:   
    "abc" and "cba" has the same hash value.   
    calculate_hash("abc") = 97 + 98 + 99 = 294.  
    calculate_hash("cba") = 99 + 98 + 97 = 294.  
               
* calculate_hash2(key)
  * The hash value is obteined by weighting according to the location of the characters in the string.
      example:  
      key1 = 'abc'. hash =  5^2 * ord('a') + 5^1 * ord('b') + 5^0 * ord('c') = 3014.  
      key2 = 'cba'. hash =  5^2 * ord('c') + 5^1 * ord('b') + 5^0 * ord('a') = 3062.  
      Though they have the same characters, but they have different hash value!　
      
* calculate_hash3(key)
  * The hash value is obtained by using the fact that the maximum value of the ASCII code is 127.
      example:  
      key = "abc".  
      hash = 0 * 127 + 97 = 97.  
      hash = 97 * 127 + 98 = 12417.  
      hash = 12417 * 127 + 99 = 1577058. The hash value of "abc" is 1577058.   
      
      key = "cba".  
      hash = 0 * 127 + 99 = 99.   
      hash = 99 * 127 + 98 = 12671.  
      hash = 12671 * 127 + 97 = 1609314. The hash value of "cba" is 1609314.  
      
* put(self, key, value)
  * Put an item to the hash table. If the key already exists, the corresponding value is updated to a new value.  
    |key|: The key of the item.   
    |value|: The value of the item.  
    Return value: True if a new item is added. False if the key already exists and the value is updated.  
    
* get(self, key)
  * Get an item from the hash table.    
    |key|: The key.   
    Return value: If the item is found, (the value of the item, True) is returned. Otherwise, (None, False) is returned.  
    
* delete(self, key)
  * Delete an item from the hash table.  
    |key|: The key of the item.   
    Return value: True if the item is found and deleted successfully. False otherwise.  
    
* size(self)
  * Return the total number of items in the hash table.

* check_size(self)
  * Check that the hash table has a "reasonable" bucket size. The bucket size is judged "reasonable" if it is smaller than 100 or the buckets are 30% or more used.

* calculate_and_change_size()
  * Check for proper hash table bucket size. If it is too big or too small, change the bucket size and execute rehashing. 

* rehash()
  * Change the bucket size and initialize the hash table. Move all data to new hash table.

## Execution Results 
we can reduce excution time significantly by rehashing. Below are the execution times for each hash function.   
calculate_hash3() was the fastest of the three.
* calculate_hash().  
0 0.152254.  
1 0.339602.  
2 0.354653.  
3 0.674038.  
4 0.635401.  
5 1.098001.  
6 1.495625.  
7 1.533423.  
8 1.533404.  
9 1.993337.  
10 2.540876.  
11 3.147566.  
12 3.792643.  
13 4.403499.  
14 4.257330.  
15 4.502553.       
This is too slow....

* calculate_hash2().  
0 0.103034.  
1 0.105122.  
2 0.062159.  
3 0.155032.  
4 0.062839.  
5 0.063951.  
6 0.078014.  
7 0.270107.  
8 0.065485.  
9 0.088814.   
10 0.067612.  
11 0.069243.      
12 0.070101.  
13 0.130668.  
14 0.645267.  
15 0.070934.  
・・・・    
90 0.129165   
91 0.130082   
92 0.130629   
93 0.131413    
94 0.133246.  
95 0.133246.  
96 0.135062.  
97 0.138217.  
98 0.136259.  
99 0.137708.  

* calculate_hash3().  
0 0.051867.  
1 0.054452.  
2 0.034432.     
3 0.082250.  
4 0.034635.   
5 0.035213.    
6 0.044210.  
7 0.142643.  
8 0.035383.  
9 0.047506.  
10 0.035920.  
11 0.036553.  
12 0.036679.  
13 0.063513.  
14 0.311791.  
15 0.058731.  
・・・・.   
90 0.037722.   
91 0.037941.   
92 0.037885.  
93 0.301188.  
94 0.037508.  
95 0.037828.  
96 0.038123.  
97 0.037822.  
98 0.037772.  
99 0.038087.  

  
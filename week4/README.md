# Wikipedia.py
* The purpose of this code is to analyze Wikipedia pages.
## Function
* **find_longest_titles(self)**.  
  * Find the longest titles in the text file and output the title.
 
* **find_most_linked_pages(self)**.    
  * Find the most linked titles in the text file and output the title.

* **find_shortest_path(self, start, goal)**.   
  * Find the shortest path which starts with "start" and ends with "goal" by using the method of BFS.
  * return value : path from "start" to "goal".
 
* **reconstruct_path(self, predecessors, goal)**.     
  * Restore a list of page IDs via the shortest path.
  * return value : ID list of the shortest path

* **make_current_pagerank(self)**.    
  * This is a function for use with find_most_popular_pages(self,count).   
  * return value : current_pagerank ([{"ID": 0, "value": 1},{"ID": 1, "value": 1},{"ID": 2, "value": 1},,,,, )
 
* **make_new_pagerank(self)**
  * This is a function for use with find_most_popular_pages(self,count). 
  * Initialize new_pagerank and returns the new_pagerank.
  * return value : new_pagerank ([{"ID": 0, "value": 0},{"ID": 1, "value": 0},{"ID": 2, "value": 0},,,,, )

* **find_most_popular_pages(self,count)**.    
  * Calculate pagerank for each pages in the text file, and update the page rank values.      
(Repeat and output the sum for "count" times.).     
  * Sort the current_pagerank and output the sum and 10 largest values.   
  ***
  **example**:    
  python3 wikipedia.py links_medium.txt pages_medium.txt.     
             find_most_popular_pages(self,5).    
    sum: 631853.0237285082.    
    sum: 631853.0296487978.   
    sum: 631853.0359754106.   
    sum: 631853.042128303.   
    sum: 631853.0483249102.   
    {'ID': 3377, 'value': 1460.6521068300347}.   
    {'ID': 4145, 'value': 943.5356214469838}.   
    {'ID': 793034, 'value': 545.6824258987244}       
    {'ID': 332554, 'value': 520.5759180049585}.   
    {'ID': 1069779, 'value': 509.6430939076281}.   
    {'ID': 774362, 'value': 493.1789749496122}.   
    {'ID': 1789, 'value': 475.50388179298545}.   
    {'ID': 935867, 'value': 460.42955794678244}.   
    {'ID': 1491, 'value': 418.504090512349}    
{'ID': 1547, 'value': 414.726380600042}
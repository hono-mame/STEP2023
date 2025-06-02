#sort a string
def sort(input_str): 
    sorted_str = sorted(input_str)
    return ''.join(sorted_str)

#Binary search to find all anagrams
def binary_search(sorted_word, dictionary, original_word): 
    #initial value
    left = 0
    right = len(dictionary) - 1
    answer = []
    count = 0

    #repeat until array is empty
    while left <= right:

        #get central index
        mid = (right + left) // 2

        #if the value is in the middle and is not same as the original word
        if (dictionary[mid][0] == sorted_word) & (dictionary[mid][0] != original_word):
            
            #add a anagram to answer
            #search backforward
            while dictionary[mid][0] == sorted_word:
                if dictionary[mid][1] != original_word:
                    answer.append(dictionary[mid][1])
                mid = mid - 1
                count = count + 1

            #search　forward
            while dictionary[mid + count + 1][0] == sorted_word:
                if dictionary[mid + count + 1][1] != original_word:
                    answer.append(dictionary[mid + count + 1][1])
                mid = mid + 1

            return answer
        
        #if the value is greater than middle
        elif dictionary[mid][0] < sorted_word:
            left = mid + 1

        #if the value is smaller than middle
        else:
            right = mid - 1

    #if not found
    return -1

#create new dictionary
def make_new_dictionary(dictionary):
    new_dictionary = []
    for word in dictionary:
        sorted_word = sort(word)
        new_dictionary.append((sorted_word,word))
    sorted_new_dictionary = sorted(new_dictionary, key=lambda x: x[0]) #1番目の要素でソート
    return sorted_new_dictionary

#read dictionary
def read_dictionary():
    with open('words.txt') as f:
        dictionary = f.read().split("\n")
        return dictionary

#return anagram
def return_anagram(string, dictionary, original_word):
    new_dictionary = make_new_dictionary(dictionary)
    anagram = binary_search(string,new_dictionary, original_word)
    return anagram


dictionary = read_dictionary()
random_word = input("Please enter a string : ")
answer = return_anagram(sort(random_word), dictionary,random_word)

if (answer == []) or (answer == -1) :
    print("No anagrams for this word exist.")
else:
    print("The anagram of",random_word,"is",answer)

#test1
#Please enter a string : live
#The anagram of live is ['veil', 'levi', 'evil', 'vile']

#test2
#Please enter a string : listen
#The anagram of listen is ['inlets', 'enlist', 'silent', 'tinsel']

#test3
#Please enter a string : 
#No anagrams for this word exist.

#test4
#Please enter a string : iwernfdfsbhsdfdfsdkfsdfe
#No anagrams for this word exist.
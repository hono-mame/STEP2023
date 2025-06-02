import sys
#count alphabets
def count_alphabets(string):
    alphabets = {}
    for char in string:
        if char.isalpha():
            alphabets[char] = alphabets.get(char, 0) + 1
    return alphabets

#make alphabets_count list
def count_alphabets_list(strings):
    alphabets_list = []
    for string in strings:
        alphabets = {}
        for char in string:
            if char.isalpha():
                alphabets[char] = alphabets.get(char, 0) + 1
        alphabets_list.append(alphabets)
    return alphabets_list

#read a dictionary
def read_dictionary():
    with open('words.txt') as f:
        dictionary = f.read().split("\n")
        return dictionary
    
#extract only the dictionary part from the tuple
def get_dictionary(dictionary):
    new_dictionary = [entry[0] for entry in dictionary]
    return new_dictionary

#add the original word after the alphabet count
def make_new_dictionary(dictionary1, dictionary2):
    new_dictionary = []
    for i in range(len(dictionary1)):
        new_entry = (dictionary1[i], dictionary2[i])
        new_dictionary.append(new_entry)
    return new_dictionary

#calculate socre
def score(word):
    SCORE = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]
    score = 0
    for character in word:
        score += SCORE[ord(character) - ord('a')]
    return score



#check if dictionary2 is a subset of dictionary1      
def is_subset(dictionary1, dictionary2):
    for key, value in dictionary1.items():
        if key not in dictionary2 or dictionary2[key] < value:
            return False
    return True


#check if it is anagram, calcurate the sum of scores
def check(new_dictionary, input):
    best_anagram = ''
    anagram_list = []
    sum_score = 0
    for test_word in input:
        max_score = 0
        for dic in new_dictionary:
            if is_subset(dic[0],test_word):
                word_score = score(dic[1])
                if word_score > max_score:
                    max_score = word_score
                    best_anagram = dic[1]
        anagram_list.append(best_anagram)
        sum_score += max_score

    with open(sys.argv[2], "w") as file:
        file.writelines(line + "\n" for line in anagram_list)
    print("Max_score:",sum_score)

#read a file
with open(sys.argv[1], 'r') as f_in:
    input_f = f_in.read().split("\n")

#Record the alphabet and number of letters used in the dictionary
new_input = [count_alphabets(text) for text in input_f]
dictionary = read_dictionary()
new_dictionary = make_new_dictionary(count_alphabets_list(dictionary),dictionary)
check(new_dictionary,new_input)
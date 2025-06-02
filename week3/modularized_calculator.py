#! /usr/bin/python3

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index - 1

def read(line, index):
    if line[index].isdigit():
        (token, index)  = read_number(line, index)
    elif line[index] == '+':
        token = {'type': 'PLUS'}
    elif line[index] == '-':
        token = {'type': 'MINUS'}
    elif line[index] == '*':
        token = {'type': 'MULTIPLICATION'}
    elif line[index] == '/':
        token = {'type': 'DIVISION'}
    elif line[index] == '(':
        token = {'type': 'left_PARENTHESES'}
    elif line[index] == ')':
        token = {'type': 'right_PARENTHESES'}
    else:
        print('Invalid character found: ' + line[index])
        exit(1)
    return token , index + 1

def tokenize(line):
    tokens = []
    index = 0
    i = 0
    while index < len(line):
        (token, index) = read(line, index)
        tokens.append(token)
    return tokens

def contains_no_parentheses(tokens):
    for token in tokens:
        if token['type'] == 'left_PARENTHESES' or token['type'] == 'right_PARENTHESES':
            return False
    return True

def calculate_in_parentheses(tokens):
    if contains_no_parentheses(tokens):
        return tokens
    index = 0
    new_tokens = []
    while tokens[index]['type'] != 'left_PARENTHESES':
        index += 1
    index_of_open_parentheses = index
    index += 1
    while tokens[index]['type'] != 'right_PARENTHESES':
        if tokens[index]['type'] == 'left_PARENTHESES':
            index_of_open_parentheses = index
        index += 1
    index_of_close_parentheses = index
    part_answer = evaluate(tokens[index_of_open_parentheses+1:index_of_close_parentheses])
    new_token = {'type': 'NUMBER', 'number': part_answer}
    new_tokens = tokens[0:index_of_open_parentheses] + [new_token] + tokens[index_of_close_parentheses+1:]
    return calculate_in_parentheses(new_tokens)


# calculate multiplication and division and returns new_tokens
def evaluate_multiplication_and_division(tokens):
    tokens.append({'type': 'PLUS'})
    new_tokens = []
    answer = 1
    index = 1
    while index < len(tokens) - 1:
            if tokens[index + 1]['type'] != 'MULTIPLICATION' and tokens[index + 1]['type'] != 'DIVISION':
                new_tokens.append(tokens[index - 1])
                new_tokens.append(tokens[index])
                index += 2
            else:
                answer *= tokens[index]['number']
                new_tokens.append({'type': 'PLUS'})
                while (tokens[index + 1]['type'] == 'MULTIPLICATION' or tokens[index + 1]['type'] ==  'DIVISION'):
                    if tokens[index + 1]['type'] == 'MULTIPLICATION':
                        answer *= tokens[index + 2]['number']
                        index += 2
                    else:
                        answer /= tokens[index + 2]['number']
                        index += 2
                    if index >= len(tokens) - 1:
                        break
                new_tokens.append({'type': 'NUMBER', 'number': answer})
                index += 2
            answer = 1
    if (tokens[index - 3]['type'] != 'MULTIPLICATION' and tokens[index - 3]['type'] != 'DIVISION'):
        if index < len(tokens):
            new_tokens.append(tokens[index - 1])
            new_tokens.append(tokens[index])
    return new_tokens



def evaluate(tokens):
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    answer = 0
    index = 1
    new_tokens = evaluate_multiplication_and_division(tokens)
    # calculate addition and substruction
    while index < len(new_tokens):
        if new_tokens[index]['type'] == 'NUMBER':
            if new_tokens[index - 1]['type'] == 'PLUS':
                answer += new_tokens[index]['number']
            elif new_tokens[index - 1]['type'] == 'MINUS':
                answer -= new_tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return answer


def test(line):
    tokens = tokenize(line)
    new_tokens = calculate_in_parentheses(tokens)
    actual_answer = evaluate(new_tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    # check addition and substruction
    test("1+2")  # only integer
    test("1.0+2.1-3") # integer and float
    # check muptiplication and division
    test("1*2/3") # only integer
    test("1.0*2.0/3.0") #only folat
    test("1*2/3.0") # integer and float
    # check basic arithmetic operations
    test("1+2*3") # only integer
    test("2*3+1.0") # integer and float
    # check parentheses
    test("(2+3)*2") #only integer and one pair of parentheses
    test("(2+(3+2)*5)+1") #only integer and two pairs of parentheses
    test("(3.0+4*(2-1))/5") #integer, float, and two pairs of parentheses
    test("(((1.5+2.5)*4)+3)*2") # three pairs of parentheses
    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    new_tokens = calculate_in_parentheses(tokens)
    answer = evaluate(new_tokens)
    print("answer = %f\n" % answer)
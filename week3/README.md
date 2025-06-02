# modularized_calculator.py
* The purpose of this code is to perform various calculations correctly.
* Addition, subtraction, multiplication and subtraction can be calculated. You can use the minimum number of parentheses required.

## Function
* read_number(line, index)
  * Read digits between marks ('+', '-', '*', '/') and return the number by token.
  * return value : token = {'type': 'NUMBER', 'number': number} , index
 
* tokenize(line, index)
  * Determine whether they are numbers or symbols and divide them into tokens. If an invalid character exists, exit.
  * return value : tokens

* read(line, index)
  * Return the appropriate token according to the symbol.
  If it is digit (= number) then token = {'type': 'NUMBER', 'number': number}.
  If the symbol is '+' then token = {'type': 'PLUS'}.   
  If the symbol is = '-' then token = {'type': 'MINUS'}.    
  If the symbol is= '*' then token = {'type': 'MULTIPLICATION'}.  
  If the symbol is= '/' then token = {'type': 'DIVISION'}.  
  If the symbol is = '(' then token = {'type': 'left_PARENTHESES'}.   
  If the symbol is = ')' then token = {'type': 'right_PARENTHESES'}. 
  * return value : token, index + 1

*contain_no_parentheses(tokens)
  * Check if the tokens contains parentheses or not, and if there is no parentheses in the tokens, return True.
 
* evaluate_calculate_in_parentheses(tokens)
  * Find one pair of parentheses and calculate inside of them, and substitute it into answer and remove the tokens of the parentheses. The result of the calcuoation is then added as token({'type': 'NUMBER', 'number': answer}) to new_tokens.
  * This is a recursive function and runs until all parentheses are processed.
  * return value : tokens (← token with all parentheses processed)

* evaluate_multiplication_and_division(tokens)
  * Find '*' and '/' and perform multiplication and division, and substitute it into answer.　The result of the calculation is then added as token({'type': 'NUMBER', 'number': answer}) to new_tokens.
  * return value : new_tokens

* evaluate(tokens)
  * Find '+' and '-' and perform addition and subtraction. And substitute it into answer.
  * return value : answer
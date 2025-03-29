Lexical Analyzer - Overview

This program is a simple lexical analyzer that reads an arithmetic expression from a file and converts it into tokens. Tokens are classified into identifiers, numbers, operators, and parentheses. The program processes the input character by character, groups related characters into lexemes, and assigns a token type to each lexeme.


---

How the Program Works

1. Reads Input:

Opens a file (front.in) containing an arithmetic expression.

Reads characters one by one.



2. Classifies Characters:

Letters (A-Z, a-z): Treated as identifiers (e.g., x, sum).

Digits (0-9): Treated as integer literals (e.g., 10, 47).

*Operators (+, -, , /): Recognized and assigned specific token codes.

Parentheses (()): Identified as grouping symbols.

Whitespace: Skipped.



3. Token Generation:

The program forms lexemes (valid symbols in the expression).

Uses a lookup function to identify operators and parentheses.

Outputs each token along with its lexeme.





---

Example Execution

Input Expression (front.in)

x * (y - 10) / 5

Program Output

Next token is: 11, Next lexeme is x  
Next token is: 23, Next lexeme is *  
Next token is: 25, Next lexeme is (  
Next token is: 11, Next lexeme is y  
Next token is: 22, Next lexeme is -  
Next token is: 10, Next lexeme is 10  
Next token is: 26, Next lexeme is )  
Next token is: 24, Next lexeme is /  
Next token is: 10, Next lexeme is 5  
Next token is: -1, Next lexeme is EOF

This output confirms that the program correctly identifies variables, numbers, and operators.


---

Conclusion

This lexical analyzer serves as a basic tokenizer for arithmetic expressions. It can be extended for more complex expressions, including floating-point numbers and additional operators.

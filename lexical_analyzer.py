#include <iostream>
#include <cctype>
#include <cstring>

using namespace std;

/* Global declarations */
int charClass; // Stores the class of the current character (LETTER, DIGIT, UNKNOWN, EOF)
char lexeme[100]; // Stores the currently forming lexeme
char nextChar; // Stores the next character to be processed
int lexLen; // Stores the length of the current lexeme
int token; // Stores the current token
int nextToken; // Stores the next token
string input; // Stores the user input
int inputPos = 0; // Position tracker for reading input

/* Function declarations */
void addChar(); // Adds nextChar to lexeme
void getChar(); // Reads the next character from input
void getNonBlank(); // Skips whitespace characters
int lex(); // Lexical analyzer function

/* Character classes */
#define LETTER 0
#define DIGIT 1
#define UNKNOWN 99

/* Token codes */
#define INT_LIT 10
#define IDENT 11
#define ASSIGN_OP 20
#define ADD_OP 21
#define SUB_OP 22
#define MULT_OP 23
#define DIV_OP 24
#define LEFT_PAREN 25
#define RIGHT_PAREN 26

/* lookup - Function to identify operators and parentheses */
int lookup(char ch) {
    switch (ch) {
        case '(': addChar(); nextToken = LEFT_PAREN; break;
        case ')': addChar(); nextToken = RIGHT_PAREN; break;
        case '+': addChar(); nextToken = ADD_OP; break;
        case '-': addChar(); nextToken = SUB_OP; break;
        case '*': addChar(); nextToken = MULT_OP; break;
        case '/': addChar(); nextToken = DIV_OP; break;
        default: addChar(); nextToken = EOF; break;
    }
    return nextToken;
}

/* addChar - Adds nextChar to lexeme */
void addChar() {
    if (lexLen <= 98) { // Ensures lexeme does not exceed max length
        lexeme[lexLen++] = nextChar;
        lexeme[lexLen] = '\0'; // Null-terminate the lexeme
    } else {
        cout << "Error - lexeme is too long" << endl;
    }
}

/* getChar - Reads the next character from input */
void getChar() {
    if (inputPos < input.length()) {
        nextChar = input[inputPos++]; // Read next character
        if (isalpha(nextChar)) {
            charClass = LETTER; // Identify as a letter
        } else if (isdigit(nextChar)) {
            charClass = DIGIT; // Identify as a digit
        } else {
            charClass = UNKNOWN; // Identify as an unknown character (operator or symbol)
        }
    } else {
        charClass = EOF; // Mark as end of input
    }
}

/* getNonBlank - Skips whitespace characters */
void getNonBlank() {
    while (isspace(nextChar)) { // Check for spaces, tabs, newlines
        getChar(); // Read next character
    }
}

/* lex - Lexical analyzer */
int lex() {
    lexLen = 0; // Reset lexeme length
    getNonBlank(); // Skip whitespace
    switch (charClass) {
        /* Parse identifiers (variables like x, y, total) */
        case LETTER:
            addChar();
            getChar();
            while (charClass == LETTER || charClass == DIGIT) { // Allow alphanumeric names
                addChar();
                getChar();
            }
            nextToken = IDENT;
            break;
        
        /* Parse integer literals (numbers like 47, 10, 5) */
        case DIGIT:
            addChar();
            getChar();
            while (charClass == DIGIT) { // Continue reading digits
                addChar();
                getChar();
            }
            nextToken = INT_LIT;
            break;
        
        /* Parse operators and parentheses */
        case UNKNOWN:
            lookup(nextChar); // Identify token
            getChar(); // Move to next character
            break;
        
        /* Handle EOF */
        case EOF:
            nextToken = EOF;
            strcpy(lexeme, "EOF");
            break;
    }
    /* Output the identified token and lexeme */
    cout << "Next token is: " << nextToken << ", Next lexeme is " << lexeme << endl;
    return nextToken;
}

/* Main function */
int main() {
    cout << "Enter an arithmetic expression: ";
    getline(cin, input); // Read input from user
    inputPos = 0; // Reset position counter
    getChar(); // Read first character
    do {
        lex(); // Call lexical analyzer
    } while (nextToken != EOF); // Continue until end of input
    return 0;
}

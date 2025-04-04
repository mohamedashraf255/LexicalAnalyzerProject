﻿#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int charClass;
char lexeme[100];
char nextChar;
int lexLen;
int nextToken;
string input;
int inputPos = 0;

void addChar();
void getChar();
void getNonBlank();
int lex();

#define LETTER 0
#define DIGIT 1
#define UNKNOWN 99
#define INT_LIT 10
#define IDENT 11
#define ASSIGN_OP 20
#define ADD_OP 21
#define SUB_OP 22
#define MULT_OP 23
#define DIV_OP 24
#define LEFT_PAREN 25
#define RIGHT_PAREN 26

int lookup(char ch) {
    switch (ch) {
    case '(': addChar(); nextToken = LEFT_PAREN; break;
    case ')': addChar(); nextToken = RIGHT_PAREN; break;
    case '+': addChar(); nextToken = ADD_OP; break;
    case '-': addChar(); nextToken = SUB_OP; break;
    case '*': addChar(); nextToken = MULT_OP; break;
    case '/': addChar(); nextToken = DIV_OP; break;
    case '=': addChar(); nextToken = ASSIGN_OP; break;
    default: addChar(); nextToken = UNKNOWN; break;
    }
    return nextToken;
}

void addChar() {
    if (lexLen < 98) {
        lexeme[lexLen++] = nextChar;
        lexeme[lexLen] = '\0';
    }
    else {
        cout << "Error - lexeme is too long" << endl;
    }
}

void getChar() {
    if (inputPos < input.length()) {
        nextChar = input[inputPos++];
        if (isalpha(nextChar)) {
            charClass = LETTER;
        }
        else if (isdigit(nextChar)) {
            charClass = DIGIT;
        }
        else {
            charClass = UNKNOWN;
        }
    }
    else {
        charClass = -1;  // نهاية الإدخال
        nextChar = '\0';
    }
}

void getNonBlank() {
    while (isspace(nextChar)) {
        getChar();
    }
}

int lex() {
    lexLen = 0;
    getNonBlank();
    switch (charClass) {
    case LETTER:
        addChar();
        getChar();
        while (charClass == LETTER || charClass == DIGIT) {
            addChar();
            getChar();
        }
        nextToken = IDENT;
        break;

    case DIGIT:
        addChar();
        getChar();
        while (charClass == DIGIT) {
            addChar();
            getChar();
        }
        nextToken = INT_LIT;
        break;

    case UNKNOWN:
        lookup(nextChar);
        getChar();
        break;

    case -1:
        nextToken = -1;
        strcpy_s(lexeme, sizeof(lexeme), "EOF");
        break;
    }

    cout << "Next token is: " << nextToken << ", Next lexeme is: " << lexeme << endl;
    return nextToken;
}

int main() {
    cout << "Enter an arithmetic expression: ";
    getline(cin, input);
    inputPos = 0;
    getChar();
    do {
        lex();
    } while (nextToken != -1);
    return 0;
}

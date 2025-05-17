grammar g; // Name of the grammar for subset G of J

// Parser Rules
// entry point: one or more statements, then end-of-file
root
     : stmt+ EOF
     ;

stmt 
     : 'help'            # help
     | ID ASSIGN expr    # assignment
     | expr              # exprStmt
     ;

// expressions are parsed right-to-left, all ops same precedence
expr
     : operand (binaryop expr)? // operand then optionally “+ expr” etc. so we can do '1 1 1'
     ;

// an operand can be a vector literal, a single number, a variable, or parenthesized
operand
    : vector             // a list of numbers, e.g. “1 2  3”
    | scalar             // scalar
    | ID                 // variable name
    | '(' expr ')'       // grouping, like “(1 + 2)”
    ;

// a vector is two or more sacalars in a row
// capture space-separated numbers as one list
vector
    : scalar scalar+  // ex: 1 2 3
    ;

// single number
scalar
     : INT ;

// binary operators
binaryop
     : '+'     # SUM
     | '-'     # SUB
     | '*'     # MUL
     | '/'     # DIV
     | '|'     # MOD
     | '^'     # POW
     ;

// Lexer Rules
ASSIGN: '=:';               // Assignment operator
INT: [0-9]+;             // Integer numbers
ID: [a-zA-Z_][a-zA-Z0-9_]*; // Identifiers
WS: [ \t\r\n]+ -> skip;     // Whitespace (ignored)
COMMENT : 'NB.' ~[\r\n]* -> skip ;
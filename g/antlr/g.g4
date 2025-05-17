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

expr
     : operand (binaryOp expr)?    # binaryexpr
     ;

// an operand can be a vector literal, a single number, a variable, or parenthesized
operand
    : vector             // a list of numbers, e.g. “1 2  3”
    | scalar             // scalar
    | ID                 // variable name
    | '(' expr ')'       // grouping, like “(1 + 2)”
    ;

// single number
scalar
     : unaryOp? INT ;

// a vector is two or more sacalars in a row
// capture space-separated numbers as one list
vector
    : scalar scalar+  // ex: 1 2 3
    ;

// unary operator
unaryOp
     : binaryOp ':'
     | '_'
     | ']'
     | '#'
     | 'i.'
     ;

// binary operators
binaryOp
     : '+'
     | '-'
     | '*'
     | '%'
     | '|'
     | '^'
     | '/'
     | ','
     ;         // we could expand with CHAR to be able to define custom operators?

// Lexer Rules
ASSIGN: '=:';               // Assignment operator
INT: [0-9]+;             // Integer numbers
ID : [a-zA-Z] [a-zA-Z0-9_]* ;
WS: [ \t\r\n]+ -> skip;     // Whitespace (ignored)
COMMENT : 'NB.' ~[\r\n]* -> skip ;
grammar g; // Name of the grammar for subset G of J

// Parser Rules
// entry point: one or more statements, then end-of-file
root
     : stmt+ EOF
     ;

stmt
     : ID ASSIGN expr    # assignment
     | expr              # exprStmt
     ;

// expressions are parsed right-to-left, all ops same precedence
expr
     : operand (binaryop expr)? // operand then optionally “+ expr” etc. so we can do '1 1 1'
     ;

// an operand can be a vector literal, a single number, a variable, or parenthesized
operand
    : vector             // a list of numbers, e.g. “1 2 3”
    | NUMBER             // single integer
    | ID                 // variable name
    | '(' expr ')'       // grouping, like “(1 + 2)”
    ;

// a vector is one or more NUMBER in a row
// capture space-separated numbers as one list
vector
    : NUMBER+  // ex: 1 2 3
    ;

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
NUMBER: [0-9]+;             // Integer numbers
ID: [a-zA-Z_][a-zA-Z0-9_]*; // Identifiers
WS: [ \t\r\n]+ -> skip;     // Whitespace (ignored)
COMMENT : 'NB.' ~[\r\n]* -> skip ;
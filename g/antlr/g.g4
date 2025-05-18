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

flipOp
  : binaryOp FLIP
  ;

expr
  : operand ((binaryOp | flipOp) expr)? # binaryexpr
  ;

operand 
    : unaryOp operand   # unaryexpr
    | unit              # unitexpr
    ;

// a unit can be a vector literal, a single number, a variable, or parenthesized
unit
    : vector             // a list of numbers, e.g. “1 2  3”
    | scalar             // scalar
    | ID                 // variable name
    | '(' expr ')'       // grouping, like “(1 + 2)”
    ;

// single number
scalar
    : INT ;

// a vector is two or more sacalars in a row
// capture space-separated numbers as one list
vector
    : scalar scalar+  // ex: 1 2 3
    ;

// unary operator
unaryOp
    : binaryOp ':'  # makeunary // converts verb to unary (i)
    | binaryOp '/'  # fold      // fold (i)
    | '_'           # NEGATE    // scalar negation ()
    | ']'           # IDENTITY  // identity
    | '#'           # LEN       // len
    | 'i.'          # IOTA      // iota like go
    ;

// binary operators
binaryOp
    : '+'     // sum      (i)  
    | '-'     // sub      (i)  
    | '*'     // mult     (i)  
    | '%'     // div      (i)  
    | '|'     // mod      (i)  
    | '^'     // pow      (i)  
    | '>='    // gte      (i)  
    | '<='    // lte      (i)  
    | '<>'    // dif      (i)  
    | '>'     // gt       (i)
    | '<'     // lt       (i)
    | '='     // eq       (i)
    | ','     // concat   (i)  
    | '@:'    // compose  ()      
    | '#'     // filter   (i)  
    | '{'     // access   (i)  
    ;

// Lexer Rules
FLIP: '~';
ASSIGN: '=:';               // Assignment operator
INT: [0-9]+;             // Integer numbers
ID : [a-zA-Z] [a-zA-Z0-9_]* ;
WS: [ \t\r\n]+ -> skip;     // Whitespace (ignored)
COMMENT : 'NB.' ~[\r\n]* -> skip ;
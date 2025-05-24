grammar g;

root
    : NEWLINE? (stmt NEWLINE*)* EOF
    ;

stmt 
    : ID ASSIGN (expr | compose)     # assgexpr
    | expr               # exprstmt
    | HELP               # help
    ;

compose
    : expr ( '@:' compose )?
    ;

expr
    : ID expr                             # applyexpr
    | operand ((binaryOp | flipOp) expr)? # binaryexpr
    ;

operand 
    : unaryOp (expr)?      # unaryexpr
    | unit                 # unitexpr
    ;

unit
    : vector
    | scalar
    | ID
    | '(' expr ')'
    ;

flipOp
    : binaryOp FLIP   # flipped
    ;

scalar
    : (NEGATIVE)? INT ;

vector
    : scalar scalar+  // ex: 1 2 3
    ;

// unary operator
unaryOp
    : binaryOp ':'  # makeunary
    | binaryOp '/'  # fold
    | '-'           # NEGATE
    | ']'           # IDENTITY
    | '#'           # LEN
    | 'i.'          # IOTA
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
    | '#'     // filter   (i)  
    | '{'     // access   (i)  
    ;

NEGATIVE:
    '_';
FLIP:
    '~';
ASSIGN:
    '=:';
INT:
    [0-9]+;
ID:
    [a-zA-Z] [a-zA-Z0-9_]* ;
NEWLINE:
    '\r'? '\n' ;
WS:
    [ \t\r\n]+ -> skip;
COMMENT:
    'NB.' ~[\r\n]* -> skip ;
HELP:
    'help';
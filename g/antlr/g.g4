grammar g;

root
    : stmt+ EOF
    | 'help'            # help
    ;

funcdecl
  : (binaryOp | unaryOp | IDENTITY) ( '@:' funcdecl )+
  ;

flipOp
  : binaryOp FLIP   # flipped
  ;

stmt 
    : ID ASSIGN funcdecl # assgFuncdecl
    | ID ASSIGN expr     # assgExpr
    | expr               # exprStmt
    ;

expr
  : operand ((binaryOp | flipOp) expr)? # binaryexpr
  ;

operand 
    : unaryOp operand   # unaryexpr
    | unit              # unitexpr
    ;

unit
    : vector
    | scalar
    | ID
    | '(' expr ')'
    ;

scalar
    : INT ;

vector
    : scalar scalar+  // ex: 1 2 3
    ;

// unary operator
unaryOp
    : binaryOp ':'  # makeunary
    | binaryOp '/'  # fold
    | '_'           # NEGATE
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
    | '@:'    // compose  ()      
    | '#'     // filter   (i)  
    | '{'     // access   (i)  
    ;

// Lexer Rules
FLIP:
    '~';
ASSIGN:
    '=:';
INT:
    [0-9]+;
ID:
    [a-zA-Z] [a-zA-Z0-9_]* ;
WS:
    [ \t\r\n]+ -> skip;
COMMENT:
    'NB.' ~[\r\n]* -> skip ;
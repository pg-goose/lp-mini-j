grammar exprs;

root : stmt ;

stmt : SYM ASSIG expr    # assignement
     | WRITE expr        # write
     | expr              # exprStmt
     ;

expr : <assoc=right> expr '^' expr    # pow
     | expr '*' expr                  # mult
     | expr '/' expr                  # div
     | expr '+' expr                  # sum
     | expr '-' expr                  # sub
     | '-' expr                       # negative
     | '(' expr ')'                   # parenthesis
     | NUM                            # number
     | SYM                            # symbol
     ;

// keywords
WRITE : 'write' ;

ASSIG : ':=' ;
NUM   : [0-9]+ ;
SYM   : [a-zA-Z\u0080-\u00FF]+ ;
WS    : [ \t\n\r]+ -> skip ;


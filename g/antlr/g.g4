grammar g;

root : expr             // l'etiqueta ja és root
     ;
expr : expr '+' expr    # suma
     | NUM              # numero
     ;
NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ;
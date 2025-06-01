# G - Mini J

Interpret del llenguatge G (subconjunt de J) en Python.

> Autor: Pau Galopa Barroso (gh: @aGoose)

# Requisits
- make
- python 3.10^

_requirements.txt_
```
antlr4-python3-runtime==4.13.2
antlr4-tools==0.2.2
install-jdk==1.1.0
```

# Instal·lació
```
git clone https://github.com/pg-goose/lp-mini-j.git

cd lp-mini-j

pip install -r requirements.txt
```

# Ús
Previ a qualsevol ús, cal compilar el fitxer de gramàtica `g.g4` amb `make`.

- `make clean` per netejar els fitxers generats.
- `python3 g.py` per accedir al REPL 
- `python3 g.py <fitxer.j>` per executar un fitxer J.

# Fitxers
```
lp-mini-j/
├── base.j
├── base.out
├── extra.j
├── extra.out
├── g
│   ├── antlr
│   │   └── g.g4
│   ├── core
│   │   ├── binary_operatos.py
│   │   ├── error.py
│   │   ├── evaluator.py
│   │   ├── result.py
│   │   ├── symbol_table.py
│   │   └── unary_operators.py
│   ├── __init__.py
│   └── repl
│       └── __init__.py
├── g.py
├── LICENSE
├── makefile
├── README.md
└── requirements.txt
```

- `base.j` i `extra.j` són exemples de fitxers J, jocs de proves.
- `base.out` i `extra.out` són els resultats esperats de l'execució dels fitxers J.
- `g/antlr/g.g4` és el fitxer de gramàtica del llenguatge G.
- `g/core/` conté les classes que implementen la lògica del llenguatge G.
- `g/repl/` conté la lògica del REPL.
- `g.py` és el punt d'entrada del programa, on es gestiona la lògica de la línia d'ordres i el REPL.

# Errors Coneguts
- Composició de funcions amb parentesis no funciona correctament, apareix com error sintactic.
- La mida d'un escalar no es pot calcular, apareix com error
- Un cop trobat un error sintàctic, el programa no continua executant-se. En el REPL si.

# Desicions de disseny

Per a la implementació de l’evaluador principal, he optat per seguir un disseny basat en Mixins per separar en mòduls les diferents funcionalitats. Bàsicament, construïm l’evaluador a partir d’heretar la funcionalitat implementada en cada mixin. Comencem tenint un base `BaseMixin` que conté lògica per gestionar els símbols, aplicar funcions... Després, un mixin per a diferents grups d’expressions: `BinaryMixin`, `OperandMixin`, etc. Finalment, `GEvaluator` hereta de tots aquests mixins.

He optat per aquesta solució perquè permet escalar fàcilment. Afegir nous operadors o tipus d’expressions només requereix ampliar el mixin adequat i regenerar el visitador ANTLR si cal. Reconeixo que la definició dels mixins no és perfecta ja que la gramatica a cambiat bastant en les ultimes iteracions i ja no he tingut temps de refactoritzar-ho acorde, però crec que és una solució interessant per a un projecte d’aquest tipus.

# Autor

Pau Galopa Barroso
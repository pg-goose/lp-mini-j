ANTLR_DIR := ./g/antlr
FLAGS     := -Dlanguage=Python3 -no-listener -visitor

all: 
	@echo "Generating ANTLR files..."
	antlr4 $(FLAGS) $(ANTLR_DIR)/g.g4
	@echo "Generated files in $(ANTLR_DIR)"

clean:
	rm g/antlr/*.interp
	rm g/antlr/*.tokens
	rm g/antlr/*.py

.PHONY: all clean
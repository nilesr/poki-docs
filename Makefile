all:
	python3 generate.py
clean:
	rm -rf generated/*.html
.PHONY: all clean

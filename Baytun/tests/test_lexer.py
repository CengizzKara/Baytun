from baytun.lexer import tokenize
assert tokenize("seto x = 5") == ["SETO", "x", "=", "5"]
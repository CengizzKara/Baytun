def tokenize(line):
    tokens = line.replace('(', ' ( ').replace(')', ' ) ').replace('{', ' { ').replace('}', ' } ').split()
    tokens = [t.upper() if t in ["seto", "reveal", "compute", "judge", "loop", "craft", "yield", "ask", "morph", "check", "stacko", "pusho", "takeo", "sliceo", "mergeo", "randio", "waito", "timeo", "logo", "swapo", "repeat"] else t for t in tokens]
    return tokens
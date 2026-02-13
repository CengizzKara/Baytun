# Baytun Programming Language

Baytun is an experimental programming language built on a pure Python interpreter with a unique command-based syntax inspired by Middle Eastern terminology. It is designed for learning how programming languages work internally while providing a distinctive coding style.

Baytun focuses on simplicity, readability, and extensibility.

---

# Features

- Custom command syntax
- Pure Python interpreter
- Interactive REPL
- Script execution (.bt files)
- Cross-platform support (Windows & Linux)
- Modular architecture

---

# Installation

## Install Python

Download Python:

https://www.python.org

Verify installation:

### Windows
```
python --version
```

### Linux
```
python3 --version
```

---

# Download Baytun

Using Git:

```
git clone https://github.com/yourusername/Baytun.git
cd Baytun
```

Or download ZIP and extract.

---

# Usage Guide

## Run Interactive REPL

### Windows
```
python -m baytun.repl
```

or

```
cd baytun
python repl.py
```

### Linux
```
python3 -m baytun.repl
```

or

```
cd baytun
python3 repl.py
```

---

## Run a Script File

```
python -m baytun examples/basic.bt
```

Linux:

```
python3 -m baytun examples/basic.bt
```

---

# Baytun Command Reference

## Variable & Data Commands

### seto — Assign variable
```
seto x = 10
seto name = "Baytun"
```

### store — Input from user
```
store username
```

### convert — Type conversion
```
convert x to string
convert text to number
```

---

## Output

### reveal — Print output
```
reveal x
reveal "Hello World"
```

---

## Math & Logic

### compute — Arithmetic operations
```
compute x + 5
compute 10 * 2
compute (x + 3) / 2
```

### compare — Compare values
```
compare x == y
compare x > 10
compare x < y
```

---

## Control Flow

### judge — Conditional execution
```
judge x > 5 {
    reveal x
}
```

### loop — Repeat block
```
loop 3 {
    reveal "Hello"
}
```

---

## Functions

### craft — Define function
```
craft add(a, b) {
    yield a + b
}
```

### invoke — Call function
```
invoke add(5, 3)
```

### yield — Return value
```
yield result
```

---

## Advanced Commands

### append — Add to variable
```
append x 5
```

### remove — Remove from variable
```
remove x 2
```

### swap — Swap variables
```
swap x y
```

### check — Check existence
```
check x
```

### clear — Clear variable
```
clear x
```

---

# Example Program

```
seto x = 5
seto y = 7

craft add(a, b) {
    yield a + b
}

seto result = invoke add(x, y)

judge result > 10 {
    reveal "Large result"
}

loop 2 {
    reveal result
}
```

---

# Project Structure

```
Baytun/
│
├─ baytun/
│   ├─ __init__.py
│   ├─ lexer.py
│   ├─ parser.py
│   ├─ interpreter.py
│   ├─ repl.py
│   └─ utils.py
│
├─ examples/
├─ tests/
├─ docs/
└─ README.md
```

---

# Requirements

- Python 3.8+
- No external libraries required

---

# Purpose

Baytun is designed for:

- Learning programming language design
- Understanding interpreters
- Experimenting with syntax creation
- Educational projects

---

# License

Open-source for educational and experimental use.

---

# Author

Baytun Language Project

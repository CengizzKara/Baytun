# baytun/repl.py
from baytun.interpreter import execute_line

def repl():
    while True:
        try:
            line = input("Baytun> ")
            if line.lower() in ["exit", "quit"]:
                break
            execute_line(line)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    repl()
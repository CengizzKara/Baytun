from baytun.lexer import tokenize
from baytun.parser import parse
from baytun.utils import is_number, to_number
import random
import time

variables = {}

def execute_line(line):
    tokens = tokenize(line)
    parsed = parse(tokens)
    if not parsed:
        return
    cmd = parsed[0]

    if cmd == "SETO":
        var_name = parsed[1]
        if parsed[2] == "=":
            try:
                value = to_number(parsed[3])
            except:
                value = parsed[3]
            variables[var_name] = value

    elif cmd == "REVEAL":
        output = []
        for token in parsed[1:]:
            if token in variables:
                output.append(str(variables[token]))
            else:
                output.append(str(token))
        print(" ".join(output))

    elif cmd == "COMPUTE":
        expr = " ".join(parsed[1:])
        for var in variables:
            expr = expr.replace(var, str(variables[var]))
        variables["_"] = eval(expr)

    elif cmd == "JUDGE":
        condition = " ".join(parsed[1:])
        for var in variables:
            condition = condition.replace(var, str(variables[var]))
        variables["_COND_"] = eval(condition)

    elif cmd == "LOOP":
        condition = " ".join(parsed[1:])
        loop_lines = []
        in_block = False
        for token in parsed[1:]:
            if token == "{":
                in_block = True
                continue
            if token == "}":
                in_block = False
                continue
            if in_block:
                loop_lines.append(token)
        while eval(" ".join([variables.get(t, t) for t in parsed[1:]])):
            for line in loop_lines:
                execute_line(line)

    elif cmd == "CRAFT":
        func_name = parsed[1].lower()
        args_start = parsed.index("(") + 1
        args_end = parsed.index(")")
        args = parsed[args_start:args_end]
        variables[func_name] = {"args": args, "lines": []}

    elif cmd == "YIELD":
        expr = " ".join(parsed[1:])
        for var in variables:
            expr = expr.replace(var, str(variables[var]))
        variables["_"] = eval(expr)

    elif cmd == "ASK":
        prompt = " ".join(parsed[1:])
        inp = input(prompt + " ")
        try:
            variables["_"] = to_number(inp)
        except:
            variables["_"] = inp

    elif cmd == "MORPH":
        var = parsed[1]
        typ = parsed[-1].lower()
        if typ == "int":
            variables[var] = int(variables[var])
        elif typ == "float":
            variables[var] = float(variables[var])
        elif typ == "str":
            variables[var] = str(variables[var])

    elif cmd == "CHECK":
        condition = " ".join(parsed[1:])
        for var in variables:
            condition = condition.replace(var, str(variables[var]))
        variables["_"] = eval(condition)

    elif cmd == "STACKO":
        var_name = parsed[1]
        list_value = eval(" ".join(parsed[3:]))
        variables[var_name] = list_value

    elif cmd == "PUSHO":
        stack_name = parsed[1]
        value = to_number(parsed[2]) if parsed[2].isdigit() else parsed[2]
        variables[stack_name].append(value)

    elif cmd == "TAKEO":
        stack_name = parsed[1]
        variables["_"] = variables[stack_name].pop()

    elif cmd == "SLICEO":
        stack_name = parsed[1]
        start = int(parsed[2])
        end = int(parsed[3])
        variables["_"] = variables[stack_name][start:end]

    elif cmd == "MERGEO":
        stack1 = parsed[1]
        stack2 = parsed[2]
        variables["_"] = variables[stack1] + variables[stack2]

    elif cmd == "RANDIO":
        start = int(parsed[1])
        end = int(parsed[2])
        variables["_"] = random.randint(start, end)

    elif cmd == "WAITO":
        time.sleep(int(parsed[1]))

    elif cmd == "TIMEO":
        variables["_"] = time.time()

    elif cmd == "LOGO":
        output = []
        for token in parsed[1:]:
            if token in variables:
                output.append(str(variables[token]))
            else:
                output.append(str(token))
        print("LOG:", " ".join(output))

    elif cmd == "SWAPO":
        var1 = parsed[1]
        var2 = parsed[2]
        variables[var1], variables[var2] = variables[var2], variables[var1]

    elif cmd == "REPEAT":
        times = int(parsed[1])
        block_start = parsed.index("{") + 1
        block_end = parsed.index("}")
        block = parsed[block_start:block_end]
        for _ in range(times):
            execute_line(" ".join(block))
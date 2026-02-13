from baytun.interpreter import execute_line, variables
execute_line("seto x = 10")
execute_line("seto y = 5")
execute_line("compute x + y")
assert variables["_"] == 15
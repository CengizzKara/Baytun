def is_number(value):
    return isinstance(value, (int, float))

def to_number(value):
    try:
        if '.' in str(value):
            return float(value)
        else:
            return int(value)
    except:
        raise ValueError(f"Cannot convert '{value}' to number")
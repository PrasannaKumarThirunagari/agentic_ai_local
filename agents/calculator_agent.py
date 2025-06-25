import ast
import operator as op

# Supported operators only
ops = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
}

def eval_expr(expr):
    def _eval(node):
        if isinstance(node, ast.Num):  # Numbers like 3, 4
            return node.n
        elif isinstance(node, ast.BinOp):  # e.g. 3 + 4
            return ops[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp):  # e.g. -5
            return ops[type(node.op)](_eval(node.operand))
        else:
            raise TypeError(f"Unsupported expression: {ast.dump(node)}")

    try:
        print(f"📥 Raw expression: {expr}")  # Debug log
        parsed = ast.parse(expr, mode='eval').body
        return _eval(parsed)
    except Exception as e:
        return f"⚠️ Invalid expression: {str(e)}"

def calculate(query: str) -> str:
    # Strip all known prefixes
    prefixes = ["calculate", "eval", "compute"]
    for prefix in prefixes:
        query = query.lower().replace(prefix, "")

    expr = query.strip()
    if not expr:
        return "⚠️ No expression provided."

    result = eval_expr(expr)
    return f"🧮 Result: {result}" if not str(result).startswith("⚠️") else result

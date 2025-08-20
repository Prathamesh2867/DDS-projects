import math

def tokenize(expr):
    tokens = []
    i = 0
    n = len(expr)
    while i < n:
        c = expr[i]
        if c.isspace():
            i += 1
            continue
        if c.isdigit() or c == '.':
            j = i
            dot = 0
            while j < n and (expr[j].isdigit() or expr[j] == '.'):
                if expr[j] == '.':
                    dot += 1
                    if dot > 1:
                        raise ValueError("Invalid number with multiple dots")
                j += 1
            tokens.append(expr[i:j])
            i = j
        elif c in '+-*/^()':
            tokens.append(c)
            i += 1
        else:
            raise ValueError(f"Invalid character: {c}")
    return tokens

def to_postfix(infix_tokens):
    # Handle unary minus by converting it to 'u-'
    processed = []
    prev = None
    for t in infix_tokens:
        if t == '-':
            if prev is None or prev in ('+', '-', '*', '/', '^', '('):
                processed.append('u-')
            else:
                processed.append('-')
        else:
            processed.append(t)
        prev = t

    prec = {'u-': 4, '^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    assoc = {'u-': 'right', '^': 'right', '*': 'left', '/': 'left', '+': 'left', '-': 'left'}

    out = []
    op = []

    for t in processed:
        if t.replace('.', '', 1).isdigit():
            out.append(t)
        elif t in prec:
            while op:
                top = op[-1]
                if top in prec:
                    if (assoc[t] == 'left' and prec[t] <= prec[top]) or (assoc[t] == 'right' and prec[t] < prec[top]):
                        out.append(op.pop())
                    else:
                        break
                else:
                    break
            op.append(t)
        elif t == '(':
            op.append(t)
        elif t == ')':
            while op and op[-1] != '(':
                out.append(op.pop())
            if not op:
                raise ValueError("Mismatched parentheses")
            op.pop()
        else:
            raise ValueError(f"Unknown token: {t}")

    while op:
        top = op.pop()
        if top in ('(', ')'):
            raise ValueError("Mismatched parentheses")
        out.append(top)
    return out

def eval_postfix(postfix_tokens):
    st = []
    for t in postfix_tokens:
        if t.replace('.', '', 1).isdigit():
            st.append(float(t))
        elif t == 'u-':
            if not st:
                raise ValueError("Not enough operands for unary minus")
            a = st.pop()
            st.append(-a)
        elif t in ('+', '-', '*', '/', '^'):
            if len(st) < 2:
                raise ValueError("Not enough operands")
            b = st.pop()
            a = st.pop()
            if t == '+':
                st.append(a + b)
            elif t == '-':
                st.append(a - b)
            elif t == '*':
                st.append(a * b)
            elif t == '/':
                if b == 0:
                    raise ZeroDivisionError("Division by zero")
                st.append(a / b)
            elif t == '^':
                st.append(a ** b)
        else:
            raise ValueError(f"Unknown token in evaluation: {t}")
    if len(st) != 1:
        raise ValueError("Invalid expression")
    return st[0]

def calculate(expr):
    tokens = tokenize(expr)
    postfix = to_postfix(tokens)
    value = eval_postfix(postfix)
    return tokens, postfix, value

def main():
    print("Expression Calculator (infix -> postfix -> evaluate)")
    print("Supports +  -  *  /  ^  and parentheses, plus unary minus.")
    while True:
        try:
            s = input("\nEnter expression (or 'q' to quit): ").strip()
            if s.lower() == 'q':
                break
            tokens, postfix, value = calculate(s)
            print("Tokens: ", tokens)
            print("Postfix:", postfix)
            if value == int(value):
                print("Result: ", int(value))
            else:
                print("Result: ", value)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()

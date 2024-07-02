def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text.strip()

def tokenize(chars: str) -> list:
    return chars.replace('(', " ( ").replace(')', " ) ").split()

file_path = 'b.sexp'

text = read_text_from_file(file_path)
tokens = tokenize(text)

count1 = tokens.count('(')
count2 = tokens.count(')')



if count1 != count2:
    print("expression is wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def reculist(tokens):
    if not tokens:
        raise SyntaxError("ERROR!!!!!!!!!!!")

    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(reculist(tokens))
        tokens.pop(0)
        return L
    elif token == ')':
        raise SyntaxError("WRONG EXPRESSION")
    else:
        try:
            return int(token)
        except ValueError:
            try:
                return float(token)
            except ValueError:
                return token

def evaluate(expression, env):
    if isinstance(expression, list):
        operator = expression[0]
        if operator == '+':
            return evaluate(expression[1],env) + evaluate(expression[2],env)
        elif operator == '-':
            return evaluate(expression[1],env) - evaluate(expression[2],env)
        elif operator == '*':
            return evaluate(expression[1],env) * evaluate(expression[2],env)
        elif operator == "lambda":
                    return expression
        elif operator in env:
            lamb = env[operator]
            args = lamb[1]
            out_expr = lamb[2] 
            local_env = env.copy()  # Create a local scope for the lambda function
            for idx in range(len(args)):
                local_env[args[idx]] = evaluate(expression[idx+1], env)
            return evaluate(out_expr, local_env)



        elif operator == "let":
            for var, value in expression[1]:
                env[var] = evaluate(value, env)
            return evaluate(expression[2], env)
        elif operator == '/':
            try:
                return evaluate(expression[1],env) / evaluate(expression[2],env)
            except ZeroDivisionError:
                raise ZeroDivisionError("Division by zero")
        else:
            raise Exception("Expression is wrong", expression)
    else:
        if isinstance(expression, str):
            if expression in env:
                return env[expression]
            elif expression not in env :
                raise Exception("Undefined variable")
        elif (isinstance(expression, int) or isinstance(expression, float)):
            return expression
        else:
            raise Exception("wrong expression")     
    
parsed_expression = reculist(tokens)
print(parsed_expression)
env = {'a': 20,'b': 30}
p = evaluate(parsed_expression,env)
print(p)

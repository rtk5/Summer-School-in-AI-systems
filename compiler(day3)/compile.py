import json
import sys

inp = json.loads(sys.stdin.read())

def gen_head(header):
    fn_name = header[0]
    args = header[1:] 
    out_args = [[a, "int"] for a in args]  
    return [fn_name, "int"], out_args

def gen_body(body):
    assert body[0] == 'ret'
    expr = body[1]
    if not isinstance(expr, list):
        return [body]  
    else:
        out = []
        operator = expr[0]
        op1 = expr[1]
        op2 = expr[2]
        out_set = ['set', 'tmp', 'int']
        if operator == '+':
            out_set.append(['add', op1, op2])
        elif operator == '-':
            out_set.append(['sub', op1, op2])
        elif operator == '*':
            out_set.append(['mul', op1, op2])
        elif operator == '/':
            out_set.append(['div', op1, op2])
        else:
            raise Exception("Invalid operator enteredd !!!!")
        out.append(out_set)
        out.append(['ret', 'tmp'])
        return out

def compile(inp):
    assert inp[0] == 's-kaleidoscope'
    
    function_defns = inp[1:]
    bril_defns = []
    
    for fn in function_defns:
        assert fn[0] == 'define'
        
        header = fn[1]
        body = fn[2]
        
        head = gen_head(header)
        body = gen_body(body)
        
        bril_defns.append(["define", [head[0], *head[1]], body])
    
    return ["brilisp"] + bril_defns

try:
    output = compile(inp)
    print(json.dumps(output))
except Exception as e:
    print(f"Error: {str(e)}")

#["brilisp", ["define", [["fn", "n"], ["n", "int"]], ["ret", "n"]]]
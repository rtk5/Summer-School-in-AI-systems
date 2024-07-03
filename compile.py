import json
import sys

#["s-kaleidoscope",["define",["fn","n","m"],["ret","n"]]]

inp = json.loads(sys.stdin.read())

def gen_head(header):
    fn_name = header[0]
    args = header[1]  
    out_args = [[a, "int"] for a in args]  
    return [fn_name, "int"], out_args

def gen_body(body):
    return [body[0], body[1]]  

def compile(inp):
    assert inp[0] == 's-kaleidoscope'

    fn_definition = inp[1]
    assert fn_definition[0] == 'define'
    header = fn_definition[1]
    body = fn_definition[2]
    
    head = gen_head(header)
    body = gen_body(body)
    
    return ["brilisp", ["define", [head[0], *head[1]], body]]

try:
    output = compile(inp)
    print(json.dumps(output))
except Exception as e:
    print(f"Error: {str(e)}")

#["brilisp", ["define", [["fn", "n"], ["n", "int"]], ["ret", "n"]]]
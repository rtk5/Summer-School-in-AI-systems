import json
import sys

inp = json.loads(sys.stdin.read())

def gen_head(header):
    fn_name = header[0]
    args = header[1:]  
    out_args = [[a, "int"] for a in args]  
    return [fn_name, "int"], out_args

def gen_body(body):
    return [body[0], body[1]]  

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
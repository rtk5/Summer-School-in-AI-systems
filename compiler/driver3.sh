cat first.kal.sexp | guile llama.lisp/src/backend/utils/sexp-json.scm > inp.jason

    
cat first.kal.sexp | guile llama.lisp/src/backend/utils/sexp-json.scm | python compile.py | guile llama.lisp/src/backend/utils/json-sexp.scm > out.json
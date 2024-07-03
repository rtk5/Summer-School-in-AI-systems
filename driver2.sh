cat fibonacci_sequence.sexp | guile llama.lisp/src/backend/utils/sexp-json.scm | python llama.lisp/src/backend/brilisp.py | python llama.lisp/src/backend/llvm.py > fib.ll
clang fib.ll run.c
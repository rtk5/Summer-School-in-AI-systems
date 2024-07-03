(brilisp
    (define ((print int) (n int)))

    (define ((fib int) (n int))
        (set (g int) (const 2))
        (set (h bool) (lt n g))
        (br h lb lr)

        (label lb)
        (ret n)

        (label lr)
        (set (a int) (const 1))
        (set (b int) (const 2))
        (set (v1 int) (sub n a))
        (set (v2 int) (sub n b))
        (set (v3 int) (call fib v1))
        (set (v4 int) (call fib v2))
        (set (res int) (add v3 v4))
        (ret res)
)
    (define ((main void))
        (set (n int) (const 7))
        (set (d int) (call fib n))
        (set (tmp int) (call print d))
        (ret))

)
#include <stdio.h>

int fib(int n);

int main() {
    int n = 7;
    int d = fib(n);
    printf("%d",d);
    return 0;
}

int fib(int n) {
    if (n < 2) {
        return n;
    }
    else {
        return fib(n - 1) + fib(n - 2);
    }
}

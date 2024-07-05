#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int generate_random_number() {
    return (rand() % 5) + 1;
}

void create(int mat[], int m, int n) {
    for(int i = 0; i < m * n; i++) {
        mat[i] = generate_random_number();
    }
}

void print_matrix(int mat[], int rows, int cols) {
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            printf("%d\t", mat[i * cols + j]);
        }
        printf("\n");
    }
    printf("\n");
}

int main() {
    int a[6], b[6], c[4];  
    int m = 2, n = 3, p = 2;

    create(a, m, n);
    create(b, n, p);

    printf("Matrix A:\n");
    print_matrix(a, m, n);

    printf("Matrix B:\n");
    print_matrix(b, n, p);

    for(int i = 0; i < m * p; i++) {
        c[i] = 0;
    }

    for(int i = 0; i < m; i++) {
        for(int j = 0; j < p; j++) {
            for(int k = 0; k < n; k++) {
                c[i * p + j] += a[i * n + k] * b[k * p + j];
            }
        }
    }

    printf("Matrix C (Result):\n");
    print_matrix(c, m, p);

    return 0;
}

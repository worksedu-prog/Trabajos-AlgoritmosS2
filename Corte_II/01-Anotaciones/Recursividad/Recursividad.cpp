int factorial(int n) {
    if (n <= 1) return 1;              // CASO BASE
    return n * factorial(n - 1);       // CASO RECURSIVO
}
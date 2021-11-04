
int foo(TYPE_A x, TYPE_B y) {
    if (x <= 0) {
        return 0;
    }
    if (COND) {
        return foo(VAL_A, y) + 1;
    }
    return foo(VAL_B, y) + 1; 
}

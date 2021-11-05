
int foo(int x, int y) {
    switch(x) {
        case 0: return y+1;
        case 1: return y*2;
        case 2: return y-2;
        case 3: return y/2;
        case 4: return y&x;
        default: return y;
    }
}
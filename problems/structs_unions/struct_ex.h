/* An example node struct that could be used in a linked list.*/
typedef struct node {
    int value;
    char c;
    int *array[2];
    struct node *next;
    struct node *prev;
    char name[3];
} node_t, *nptr;
#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;

listint_t *insert_node(listint_t **head, int number);

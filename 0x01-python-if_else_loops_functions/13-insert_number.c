#include <stdlib.h>
#include "lists.h"

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node, *current, *prev;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL) {
        return NULL;  
    }

    new_node->n = number;
    new_node->next = NULL;

    current = *head;
    prev = NULL;

    while (current != NULL && current->n < number) {
        prev = current;
        current = current->next;
    }

    if (prev == NULL) {
    
        new_node->next = *head;
        *head = new_node;
    } else {
   
        prev->next = new_node;
        new_node->next = current;
    }

    return new_node;
}


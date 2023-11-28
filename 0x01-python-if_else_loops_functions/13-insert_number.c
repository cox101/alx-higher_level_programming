#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/* Definition of a singly linked list node */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/* Function to insert a number into a sorted linked list */
listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node, *current, *previous;

    /* Allocate memory for the new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL) {
        return NULL;  /* Return NULL if memory allocation fails */
    }

    /* Initialize the new node with the given number */
    new_node->n = number;
    new_node->next = NULL;

    /* If the list is empty or the new node should be inserted at the beginning */
    if (*head == NULL || (*head)->n >= number) {
        new_node->next = *head;
        *head = new_node;
        return new_node;
    }

    /* Traverse the list to find the correct position to insert the new node */
    current = *head;
    while (current != NULL && current->n < number) {
        previous = current;
        current = current->next;
    }

    /* Insert the new node into the list */
    new_node->next = current;
    previous->next = new_node;

    return new_node;
}

/* Function to print the linked list */
void print_list(listint_t *head) {
    while (head != NULL) {
        printf("%d ", head->n);
        head = head->next;
    }
    printf("\n");
}

/* Function to free the linked list */
void free_list(listint_t *head) {
    listint_t *temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

int main(void) {
    listint_t *head = NULL;

    /* Insert numbers into the sorted linked list */
    insert_node(&head, 5);
    insert_node(&head, 10);
    insert_node(&head, 15);
    insert_node(&head, 7);

    /* Print the resulting linked list */
    print_list(head);

    /* Free the linked list */
    free_list(head);

    return 0;
}


#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
/* Definition for singly-linked list. */
struct listint_s {
    int n;
    struct listint_s *next;
};

typedef struct listint_s listint_t;

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: Pointer to the head of the linked list.
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list) {
    listint_t *slow = list, *fast = list;

    while (slow && fast && fast->next) {
        slow = slow->next;        /* Move one step at a time */
        fast = fast->next->next;  /* Move two steps at a time */

        if (slow == fast) {
            /* If there is a cycle, slow and fast will meet */
            return 1;
        }
    }

    /* If we reach here, there is no cycle */
    return 0;
}

/* Example usage */
int main(void) {
    listint_t *head, *node;

    /* Create a linked list with a cycle */
    head = malloc(sizeof(listint_t));
    head->n = 1;
    head->next = NULL;

    node = malloc(sizeof(listint_t));
    node->n = 2;
    node->next = head;
    head->next = node;

    /* Check if there is a cycle */
    if (check_cycle(head)) {
        printf("There is a cycle in the linked list.\n");
    } else {
        printf("There is no cycle in the linked list.\n");
    }

    /* Free memory */
    free(head);
    free(node);

    return 0;
}

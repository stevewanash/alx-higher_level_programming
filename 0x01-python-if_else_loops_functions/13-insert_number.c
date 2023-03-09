#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds new node to sorted list
 * @head: pointer to address of the first node
 * @n: data to be input
 * 
 * Return: on success, address of new element
 * NULL on failure
 */
listint_t *insert_node(listint_t **head, const int n)
{
    listint_t *new = malloc(sizeof(listint_t));

    listint_t *nav = NULL;

    int i = 0;

    new -> n = n;

    new -> next = NULL;

    if (*head != NULL)
    {
        nav = *head;
        while (nav -> next != NULL)
        {
            if ((new -> n) > (nav -> n) && (new -> n) > ((nav -> next) -> n))
            {
                nav = nav -> next;

                i++;
            }
            else
                break;
        }
        new -> next = nav -> next;

        nav -> next = new;
    }
    else
        *head = new;

    if (nav != NULL)
        return (nav -> next);

    else if (nav == NULL)
        return (*head);
        
    else
        return (NULL);
}
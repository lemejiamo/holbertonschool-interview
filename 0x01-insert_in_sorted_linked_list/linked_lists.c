#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *
 *
 *
 */
listint_t  *insert_node(listint_t **head, int number)
{
	listint_t *copy_head = NULL;
	listint_t *new_node = NULL;

	copy_head = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return NULL;

	new_node->n = number;

	while(new_node->n >= copy_head->n)
	{
		if (copy_head->next->n < new_node->n)
			copy_head = copy_head->next;
		else
			break;
	}

	new_node->next = copy_head->next;
	copy_head->next = new_node;
	return new_node;

}
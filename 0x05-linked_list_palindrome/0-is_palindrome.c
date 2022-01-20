#include "lists.h"
/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: a pointer to the head of the linked list
 * Return: 1 if is palindrom 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL;
	listint_t *tail = NULL;
	listint_t *runner = NULL;

	if (head == NULL || *head == NULL)
		return (-1);

	temp = *head;
	runner = *head;

	while (temp != tail)
	{
		runner = temp;
		for (; runner->next != NULL && runner->next != tail;)
			runner = runner->next;

		tail = runner;

		if (tail->n != temp->n)
			return (0);

		temp = temp->next;
	}
	return (1);
}

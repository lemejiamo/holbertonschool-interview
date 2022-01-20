#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
 
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;
/**
 * struct tmp_listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct tmp_listint_s
{
	int n;
	struct listint_s *next;
	struct listint_s *back;
} tmp_listint_t;


size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);
listint_t *add_nodeint_end(listint_t **head, const int n);
int is_palindrome(listint_t **head);

#endif
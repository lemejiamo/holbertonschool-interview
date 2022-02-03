#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * race - runs the algorithm the hare and the Tortoise
 * @list: list to check
 * Returns: 0 is there is not a cycle, 1 if there is a cicle
 */
int race(listint_t **list)
{
		listint_t *rabbit = NULL;
		listint_t *tortle = NULL;
		int i = 0;

			rabbit = *list;
		tortle = rabbit;

		for (; tortle != NULL; )
		{
			for (i = 0; i < 4; i++)
			{
				if (rabbit->next == NULL)
					return (0);
				rabbit = rabbit->next;
			}
			tortle = tortle->next;

			if (tortle == rabbit)
				return (1);
		}
		return (0);
}

/**
 * check_cycle - runs the algorithm the hare and the Tortoise
 * @list: list to check
 * Returns: 0 is there is not a cycle, 1 if there is a cicle
 */
int check_cycle(listint_t *list)
{
	int is_list = 0;

	/* first case "list" exists? */
	if (!list)
	{
		return ('\0');
	}
	else
	{
		is_list = race(&list);
		if (is_list)
			return (1);
		return (0);
	}
}

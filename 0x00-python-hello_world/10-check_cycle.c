#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (!list || !list->next)
		return (0);
	turtle = list;
	hare = turtle->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);
		turlte = turtle->next;
		hare = hare->next->next;
	}
	return (0);
}

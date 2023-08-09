##include lists.h
/**
 * insert_node - Inserts a new node with a given number
 *  into a sorted linked list.
 * @head: Pointer to the pointer of the head node.
 * @number: The value of the number to insert.
 *
 * Return: Pointer to the newly inserted node,
 *  or NULL on memory allocation failure.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	current = *head;
	while (current->next && current->next->n < number)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}

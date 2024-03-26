#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: points to the list being checked
 *
 * Return: 0 for no cycle, 1 if tgere is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;
	while (temp != NULL || temp->next != list)
		temp = temp->next;
	if (temp == NULL)
		return (0);
	if (temp == list)
		return (1);
	return (0);
}

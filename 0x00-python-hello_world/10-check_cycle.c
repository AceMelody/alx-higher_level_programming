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

	if (list == NULL)
		return (0);
	temp = list;
	do
	{
		temp = temp->next;
	}while(temp != NULL || temp->next != list);
	if (temp == NULL)
		return (0);
	else if (temp == list)
		return (1);
}

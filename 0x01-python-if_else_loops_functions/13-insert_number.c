#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: points to the list
 * @number: data to be inserted
 *
 * Return: address of new node on success.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp,*n_node;

	temp = *head;
	n_node = (listint_t *) malloc(sizeof(listint_t));
	if (n_node == NULL)
		return (NULL);
	n_node->n = number;
	if (temp->next->n < number)
		temp = temp->next;
	n_node->next = temp->next;
	temp->next = n_node;
	return (n_node);
}

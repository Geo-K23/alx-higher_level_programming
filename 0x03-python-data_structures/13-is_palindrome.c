#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL;
	unsigned int j = 0, len = 0, len_list = 0, len_cyc = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	start = *head;
	len = listint_len(start);
	len_cyc = len * 2;
	len_list = len_cyc - 2;
	end = *head;

	for (; j < len_cyc; j = j + 2)
	{
		if (start[j].n != end[len_list].n)
			return (0);
		len_list = len_list - 2;
	}
	return (1);
}
/**
 * get_nodeint_at_index - Gets a node from a singly linked list
 * @head: pointer to the head of the list
 * @index: is the index to find in the linked list
 * Return: the specific node of the linked list
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int k = 0;

	if (head)
	{
		while (current != NULL)
		{
			if (k == index)
				return (current);
			current = current->next;
			++k;
		}
	}
	return (NULL);
}
/**
 * listint_len - counts the number of elements in a linked list
 * @h: is the linked list whose elements are counted
 * Return: number of elements in the linked list
 */
size_t listint_len(const listint_t *h)
{
	int length = 0;

	while (h != NULL)
	{
		++length;
		h = h->next;
	}
	return (length);
}

#include "binary_trees.h"

/**
 * binary_tree_node - create a new node in a binary tree
 * @parent: parent node to new_node
 * @value: value to new_node
 * Return: new_node or null if fail
 */
binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *new_node = NULL;

	new_node = malloc(sizeof(binary_tree_t));
	if (!new_node)
		return (NULL);

	new_node->n = value;

	if (!parent)
		return (new_node);

	new_node->parent = parent;

	if (!parent->left)
		parent->left = new_node;
	else
		parent->right = new_node;

	return (new_node);
}
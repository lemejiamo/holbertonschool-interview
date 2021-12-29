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
	new_node->left = NULL;
	new_node->right = NULL;
	new_node->parent = NULL;

	if (!parent)
		return (new_node);

	new_node->parent = parent;

	if (parent->left == NULL)
		parent->left = new_node;
	else if (parent->right == NULL)
		parent->right = new_node;
	else
		return NULL;

	return (new_node);
}

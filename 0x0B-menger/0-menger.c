#include "menger.h"

/**
 * find_space - gets a character
 * @col: column size 
 * @row: row size
 * Return: '#' or ' '
 */
char find_space(int col, int row)
{
	while (col && row)
	{
		if (col % 3 == 1 && row % 3 == 1)
		{
			return (' ');
		}
		col = col / 3, row = row / 3;
	}
	return ('#');
}

/**
 * menger - function that draws a 2D Menger Sponge
 * @level: the size of the sponge
 **/
void menger(int level)
{
	int col, row, size;

	if (level < 0)
	{
		return;
	}

	size = pow(3, level);

	for (col = 0; col < size; col++)
	{
		for (row = 0; row < size; row++)
		{
			printf("%c", find_space(col, row));
		}
		printf("\n");
	}
}
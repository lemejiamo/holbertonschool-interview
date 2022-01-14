#include "sandpiles.h"
/**
 * print_grid - Print 3x3 grid
 * @grid: 3x3 grid
 *
 */
static void print_grid(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}
/**
 * toppling - toppling a grid
 * @grid1: grid 1
 */
void toppling(int grid1[3][3])
{
	int j = 0, i = 0;
	int grid3[3][3] = {
		{0, 0, 0},
		{0, 0, 0},
		{0, 0, 0}
	};

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (grid1[i][j] > 3)
			{
				grid1[i][j] -= 4;
				/*sum up*/
				if ((i - 1) >= 0)
					grid3[i - 1][j] +=  1;

				/*sum down*/
				if ((i + 1) < 3)
					grid3[i + 1][j] +=  1;

				/*sum rigth*/
				if ((j + 1) < 3)
					grid3[i][j + 1] +=  1;

				/*sum left*/
				if ((j - 1) >= 0)
					grid3[i][j - 1] +=  1;
			}
		}
	}
	sandpiles_sum(grid1, grid3);
}

/**
 * sandpiles_sum - sum two grids
 * @grid1: grid 1
 * @grid2: grid 2
 * Return: void
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int j = 0,  i = 0, _toppling = 0;

	if (grid1 == NULL || grid2 == NULL)
		return;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			grid1[i][j] = grid1[i][j] + grid2[i][j];
			if (grid1[i][j] > 3)
				_toppling = 1;
		}
	}
	if (_toppling)
	{
		printf("=\n");
		print_grid(grid1);
		toppling(grid1);
	}
}

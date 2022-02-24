#include "slide_line.h"
/**
 * SlideLeft - function to slides to left  and merge an array of integers
 * @line: pointer to the array
 */
void SlideLeft(int *line)
{
	int position = 0, last = 0, current = 0, i = 0;


	for ( ; line[i] != '\0'; i++)
	{
		current = line[i];
		if (last == 0)
		{
			last = current;
			current = 0;
		}
		else if (current == last)
		{
			line[position] = last + current;
			last = 0;
			current = 0;
			position++;
		}
		else if (current != last)
		{
			line[position] = last;
			last = current;
			current = 0;
			position++;
		}
	}

	line[position] = last + current;
	position++;
	while (line[position] != '\0')
	{
		line[position] = 0;
		position++;
	}
}
/**
 * SlideRight - function to slides to right and merge an array of integers
 * @line: pointer to the array
 * @size: size of array
 */
void SlideRight(int *line, size_t size)
{
	int position = (size - 1), last = 0, current = 0, i = (size - 1);

	for (; i >= 0; i--)
	{
		current = line[i];
		if (last == 0)
		{
			last = current;
			current = 0;
		}
		else if (current == last)
		{
			line[position] = last + current;
			last = 0;
			current = 0;
			position--;
		}
		else if (current != last)
		{
			line[position] = last;
			last = current;
			current = 0;
			position--;
		}
	}

	line[position] = last + current;
	position--;
	while (position >= 0)
	{
		line[position] = 0;
		position--;
	}
}
/**
 * slide_line - function to slides and merge an array of integers
 * @line: pointer to the array
 * @size: array long
 * @direction: direction to merge the array
 * Return: 1 if upon success 0 upon failure
 */
int slide_line(int *line, size_t size, int direction)
{

	if (line == NULL)
		return (0);

	if (direction != SLIDE_LEFT && direction != SLIDE_RIGHT)
		return (0);

	if (direction == SLIDE_LEFT)
		SlideLeft(line);

	else if (direction == SLIDE_RIGHT)
		SlideRight(line, size);

	return (1);
}




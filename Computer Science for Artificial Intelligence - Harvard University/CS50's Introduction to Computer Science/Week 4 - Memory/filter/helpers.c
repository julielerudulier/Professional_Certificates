#include "helpers.h"
#include <math.h>
#include <tgmath.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float average = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0;
            image[i][j].rgbtBlue = round(average);
            image[i][j].rgbtGreen = round(average);
            image[i][j].rgbtRed = round(average);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float sum_red = 0;
            float sum_blue = 0;
            float sum_green = 0;
            int count = 0;
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    if (i + k < 0 || i + k >= height)
                    {
                        continue;
                    }
                    if (j + l < 0 || j + l >= width)
                    {
                        continue;
                    }
                    sum_red += temp[i + k][j + l].rgbtRed;
                    sum_blue += temp[i + k][j + l].rgbtBlue;
                    sum_green += temp[i + k][j + l].rgbtGreen;
                    count++;
                }
            }
            image[i][j].rgbtRed = round(sum_red / count);
            image[i][j].rgbtGreen = round(sum_green / count);
            image[i][j].rgbtBlue = round(sum_blue / count);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float sum_red_gx = 0;
            float sum_red_gy = 0;
            float sum_blue_gx = 0;
            float sum_blue_gy = 0;
            float sum_green_gx = 0;
            float sum_green_gy = 0;
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    if (i + k < 0 || i + k >= height)
                    {
                        continue;
                    }
                    if (j + l < 0 || j + l >= width)
                    {
                        continue;
                    }
                    sum_red_gx += temp[i + k][j + l].rgbtRed * Gx[k + 1][l + 1];
                    sum_green_gx += temp[i + k][j + l].rgbtGreen * Gx[k + 1][l + 1];
                    sum_blue_gx += temp[i + k][j + l].rgbtBlue * Gx[k + 1][l + 1];
                    sum_red_gy += temp[i + k][j + l].rgbtRed * Gy[k + 1][l + 1];
                    sum_green_gy += temp[i + k][j + l].rgbtGreen * Gy[k + 1][l + 1];
                    sum_blue_gy += temp[i + k][j + l].rgbtBlue * Gy[k + 1][l + 1];
                }
            }
            int red = round(sqrt(sum_red_gx * sum_red_gx + sum_red_gy * sum_red_gy));
            int green = round(sqrt(sum_green_gx * sum_green_gx + sum_green_gy * sum_green_gy));
            int blue = round(sqrt(sum_blue_gx * sum_blue_gx + sum_blue_gy * sum_blue_gy));

            if (red > 255)
            {
                red = 255;
            }
            if (green > 255)
            {
                green = 255;
            }
            if (blue > 255)
            {
                blue = 255;
            }

            image[i][j].rgbtRed = red;
            image[i][j].rgbtGreen = green;
            image[i][j].rgbtBlue = blue;
        }
    }
    return;
}

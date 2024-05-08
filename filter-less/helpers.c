#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    float srednia = 0;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            srednia = (int)round((image[i][j].rgbtBlue + image[i][j].rgbtRed + image[i][j].rgbtGreen) / 3.0); // wyliczamy średnią dla każdego piksela i ją zaokrąglamy

            image[i][j].rgbtBlue = srednia;
            image[i][j].rgbtRed = srednia;
            image[i][j].rgbtGreen = srednia;
        }
    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            uint8_t rgbtRedc = image[i][j].rgbtRed;
            uint8_t rgbtGreenc = image[i][j].rgbtGreen;
            uint8_t rgbtBluec = image[i][j].rgbtBlue;
            unsigned int wynik;

            wynik = (int)round(.393 * rgbtRedc + .769 * rgbtGreenc + .189 * rgbtBluec); // sepiaRed
            if (wynik > 255)                                                            // sprawdzamy czy mieści się w przedziale 8 bitowym
            {
                wynik = 255;
            }
            image[i][j].rgbtRed = wynik;
            wynik = (int)round(.349 * rgbtRedc + .686 * rgbtGreenc + .168 * rgbtBluec); // sepia Green
            if (wynik > 255)                                                            // sprawdzamy teraz żeby nie zapisać za dużej liczby do zmiennej 8 bitowej
            {
                wynik = 255;
            }
            image[i][j].rgbtGreen = wynik;
            wynik = (int)round(.272 * rgbtRedc + .534 * rgbtGreenc + .131 * rgbtBluec); // sepia Blue

            if (wynik > 255)
            {
                wynik = 255;
            }
            image[i][j].rgbtBlue = wynik;
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
             RGBTRIPLE buffor;

            for(int j=0,x=width/2;j<x;j++)//wyznaczamy środek tablicy
            {


                buffor=image[i][width-1-j];

                image[i][width-1-j]=image[i][j];

                image[i][j]=buffor;
            }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
   RGBTRIPLE copy[height][width];


   int sumaRed=0,sumaBlue=0,sumaGreen=0;
   int counter=0;
   for(int i=0;i<height;i++)//kopiujemy obraz żeby nie zmieniać wartości sąsidnich pikseli podczas wyliczania wartości
   {
        for(int j=0;j<width;j++)
        {
            copy[i][j]=image[i][j];
        }
   }
int licznikx=0,liczniky=0;
 for(int i=0;i<height;i++)
   {
        for(int j=0;j<width;j++)
        {
            for(int k=1;k<=8;k++)//obchodzimy do okoła całego piksela
            {
                if((i+1+liczniky)>=0&&(i+1+liczniky)<height&&(j+1+licznikx)>=0&&(j+1+licznikx)<width)
                {
                    sumaRed+=copy[i+1+liczniky][j+1+licznikx].rgbtRed;
                    sumaGreen+=copy[i+1+liczniky][j+1+licznikx].rgbtGreen;
                    sumaBlue+=copy[i+1+liczniky][j+1+licznikx].rgbtBlue;//liczymy sume dla czerwonego

                    counter++;
                }
                if(liczniky==-2&&licznikx>-2)//tu idziemy po kwadracie(mam nadzieję)
                {
                    licznikx--;
                }
                else if (licznikx==0&&liczniky>-2)
                {
                    liczniky--;
                }
                else if(liczniky<0&&licznikx==-2)
                {
                    liczniky++;
                }
                else if(liczniky==0&&licznikx<0)
                {
                    licznikx++;
                }

            }
            image[i][j].rgbtRed=round((sumaRed+copy[i][j].rgbtRed)/((counter+1)*1.0));
            image[i][j].rgbtGreen=round((sumaGreen+copy[i][j].rgbtGreen)/((counter+1)*1.0));//debilu nie przez ilośc kolorów czyli 3.0 ale przez ilośc bloków czyli 9 zostawiam dla potomnych razem z blokiem wewnętrznym
            image[i][j].rgbtBlue=round((sumaBlue+copy[i][j].rgbtBlue)/((counter+1)*1.0));//żeby dobrze zaokrąglić trzeba byłp pomnożyć przez 1.0
            sumaRed=0;
            sumaBlue=0;
            sumaGreen=0;
            licznikx=0;
            liczniky=0;
            counter=0;
        }
   }

    return;
}

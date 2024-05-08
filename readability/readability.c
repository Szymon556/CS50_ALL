#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int count_letter(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{   float L,S,index;
    string c = get_string("Input: ");

    L=(count_letter(c)/(float)count_words(c))*100;//obliczamy średniąi ilość liter na 100 słów

    S=(count_sentences(c)/(float)count_words(c))*100;//średnia ilość zdań na 100 słów;



    index = 0.0588 * L - 0.296 * S - 15.8;//indeks Colemana-Liau

    if(index>=16)
    {
        printf("Grade 16+\n");

    }else if(index<1)
    {
        printf("Before Grade 1\n");

    }else{

        printf("Grade %d", (int)round(index));
        printf("\n");
    }




}

int count_sentences(string text)
{
     int size,i=0,score=0;

    size=strlen(text);

    while(i!=size)
    {
        if(text[i]=='!'||text[i]=='?'||text[i]=='.')
        {
            score++;
        }

        i++;
    }

    return score;
}

int count_words(string text)
{
    int size,i=0,score=0;

    size=strlen(text);

    while(i!=size)
    {
        if(text[i]==32)
        {
            score++;
        }

        i++;
    }

    return score+1;
}


int count_letter(string text)
{

    int size,i=0,score=0;

    size=strlen(text);

        while(i!=size)
        {
            if(isalnum(text[i]))
            {
                score++;
            }


            i++;
        }

        return score;
}
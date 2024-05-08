// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];
int licznik =0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    node*cursor=table[hash(word)];

    while(cursor!=NULL)
    {
        if(strcasecmp(word,cursor->word)==0)
        {
            return true;
        }
        cursor=cursor->next;
    }


    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int zmienna =(tolower(word[0]) - 96);
    return zmienna;


}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    char *buffor=malloc(45*sizeof(char));
    node * ptr=NULL;

for(int i=0;i<N;i++)
{
    table[i]=NULL;//ustawiamy każdy wskaźnik w tablicy na NULL
}

    // TODO
    FILE * plik = fopen(dictionary,"r");//otwieramy plik

    if(plik==NULL)
    {
        return false;
    }
    node*n=NULL;//tworzy wskaźnik na pierwszy węzeł

   while(fscanf(plik,"%s",buffor)!=EOF)
   {
     n=malloc(sizeof(node));//towrzymy nowy węzeł
     if(n==NULL)
     { if(unload())
     {
         printf("\n Run out of memory");
       return false;
     }

     }

    strcpy(n->word,buffor);

    if(table[hash(buffor)]==NULL)//jeżeli dodajemy pierwszy element
    {
        table[hash(buffor)]=n;
        n->next=NULL;//Jako że dodaje elementy od przodu to pierwszy elemnt będzie ostatni

        //zapisujemy adres ostatniego elementu w zmiennej tymczasowej
    }else{

        ptr=table[hash(buffor)];//np przy drugim elemencie kopiujemy najpierw to na co wskazuje wsk tablicy czyli poprzedni element listy

        table[hash(buffor)]=n;//wsk tablicy wskazuje na najnowszy elemnet

        n->next=ptr;//ustawiamy wsk najnoszego elemnt na poprzedni
    }


 licznik++;

   }

    free(buffor);
    fclose(plik);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return licznik;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for(int i=0;i<N;i++)
    {
        node*cursor=table[i];
        node*tmp=cursor;
        while(cursor!=NULL)
        {
            cursor=cursor->next;
            free(tmp);
            tmp=cursor;
        }
    }
    return true;
}

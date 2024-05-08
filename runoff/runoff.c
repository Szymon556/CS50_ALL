#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;
int votes[MAX_CANDIDATES];
int tab_pom[MAX_CANDIDATES];
// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);
void merge_sort(int votes[],int lewy,int prawy);
void merge(int votes[],int lewy,int srodek,int prawy);
int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }

    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    for(int i=0;i<candidate_count;i++)//przeszukujemy talice imion
    {
        if(!strcmp(candidates[i].name,name))//jeśli dane imie istnieje to do tablicy preferencji daj rank
        {
           preferences[voter][rank]=i;//wpisujemy numer kandydate z tablicy imion

           return true;
        }
    }



    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{ int j=0;
    for(int i=0;i<voter_count;i++)//przeszukujemy tablice preferencji
    {
        if(candidates[preferences[i][0]].eliminated==false)//indeks kandydata z tablicy preferencji wpisujemy w tablice danego kandydata z eliminacjami i sprawdzamy czy nie został wyelminiwany
        {
            candidates[preferences[i][0]].votes++;//jeśli nie to daj mu 1 głos
        }else
        {
            while(candidates[preferences[i][j]].eliminated!=false)//w danym wierszu iterujemy kandydatów tak długo aż znajdziemy nie wyelminowanego i mu dajemy głos
            {
                j++;
            }

            candidates[preferences[i][j]].votes++;
            j=0;
        }
    }


    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{ int licznik=0;

    while(licznik<candidate_count)//przeszukuj całą tablice głosów kandydatów
    {
        if(candidates[licznik].votes>(voter_count/2))//jeśłi ktoś ma więcej głośów od połowy to wygrywa
        {
            printf("\n %s",candidates[licznik].name);
            printf("\n");
            return true;
        }

        licznik++;
    }
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
   int licznik=0,wyznacznik=candidate_count;

 while(licznik<wyznacznik)
 {
    if(candidates[licznik].eliminated==true)//jeśli kandydat jest wyelminowany to zmień wyznacznik żeby nie wyznaczać min z tej samej tablicy cały czas
    {
        wyznacznik--;
    }else
    {
        votes[licznik]=candidates[licznik].votes;//kopiujemy głosy tylko tych kandydatów co nie zostali wyelminowani
    }

    licznik++;
 }

    merge_sort(votes,0,wyznacznik-1);//używamy merg sortu żeby znaleźć najmnniejszy głos




    return votes[0];
}

void merge(int xvotes[],int lewy,int srodek,int prawy)
{
    int i,j;

    for(i=srodek+1;i>lewy;i--)//kopiujemy lewą stronę
    {
        tab_pom[i-1]=votes[i-1];//zaczynamy od srodka i idziemy do lewej
    }

    for(j=srodek;j<prawy;j++)//kopiujemy prawą stronę
    {
        tab_pom[prawy+srodek-j]=votes[j+1];//zaczynamy od prawej i idziemy do srodka można to wyobraźić sobie jakby prawa tablica byłą odwrócona na odwrót czyli zostatni element z praej strony to srodek tej tablicy
    }


    for(int k=lewy;k<=prawy;k++)
    {
        if(tab_pom[i]>tab_pom[j])
        {
            votes[k]=tab_pom[j--];
        }else{
            votes[k]=tab_pom[i++];
        }

    }

}
// Return true if the election is tied between all candidates, false otherwise
void merge_sort(int xvotes[],int lewy,int prawy)
{

        if(prawy<=lewy) return;

        int srodek=(lewy+prawy)/2;

        merge_sort(votes,lewy,srodek);
        merge_sort(votes,srodek+1,prawy);

        merge(votes,lewy,srodek,prawy);



}
bool is_tie(int min)
{
    int licznik=0;
    bool logic=false;
    while(licznik<candidate_count)//przeszukuj całą tablice głosów kandydatów
    {


            if(candidates[licznik].eliminated==false&&candidates[licznik].votes!=min)//natomiast jeżli będzie jaki kolwiek kandydat który nie został wyelminowany i ma inną wartość punktów niż min to zrwóc false poniewaz nie każdy kandydat w taki wypadku ma tyle samo punktów
            {
                logic=true;
            }

        licznik++;
    }

    if(logic==true)
    {
        return false;
    }


    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    int licznik=0;

    while(licznik<candidate_count)
    {
        if(candidates[licznik].votes==min&&candidates[licznik].eliminated==false)
        {
            candidates[licznik].eliminated=true;
        }
        licznik++;
    }
    return;
}
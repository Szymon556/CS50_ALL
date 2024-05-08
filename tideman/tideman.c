#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool check_start_end(int start, int end);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }




    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for(int i=0;i<candidate_count;i++)//powtarzamy tak długo aż znajdziemy kandydata
    {
            if(strcmp(name,candidates[i])==0)//jeżeli jest na liście kandydat wpisany przez głosującego to daj go do tablicy ranks
            {
                ranks[rank]=i;//do ranks dajemy numer danego kandydata

                return true;
            }
    }




    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{

    for(int i=0;i<candidate_count;i++)
        {

            for(int j=(i+1);j<candidate_count;j++)//możńa to sobie wyobraźić jako który kandydat nad którym wygrywa
          {
            preferences[ranks[i]][ranks[j]]++;
          }

        }
    return;

}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for(int i=0;i<candidate_count;i++)
    {
        for(int j=0;j<candidate_count;j++)
        {
            if(preferences[i][j]>preferences[j][i])
            {
                pairs[pair_count].winner=i;//dajemy indeks wygranego oraz przegranego
                pairs[pair_count].loser=j;

                pair_count++;
            }
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    int tmpwinner;
    int tmploser;
    int counter = -1;

     do
     {


     for(int i=0;i<candidate_count-2;i++)
    {
        counter=0;

        if(preferences[pairs[i].winner][pairs[i].loser]<preferences[pairs[i+1].winner][pairs[i+1].loser])//sortujemy indeksy wygranych i przegranych na podstawie zawartości macierzy
        {
                tmpwinner=pairs[i].winner;

                tmploser=pairs[i].loser;
                pairs[i].winner=pairs[i+1].winner;
                pairs[i].loser=pairs[i+1].loser;

                pairs[i+1].winner=tmpwinner;
                pairs[i+1].loser=tmploser;

                counter++;


        }
    }
     }while(counter!=0);
    return;
}

bool check_start_end(int start,int end)
{
   if(end==start)//sprawdzamy czy początek cyklu i koniec to to samo(chodzi o grafy)
   {
    return true;
   }

     for(int i=0;i<pair_count;i++)
     {wget 
        if(locked[end][i])
        {
            if(check_start_end(start,i))
            {
                return true;
            }
        }
     }

     return false;

}


// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{

        for(int i=0;i<pair_count;i++)
        {
            if(!check_start_end(pairs[i].winner,pairs[i].loser))
            {
                locked[pairs[i].winner][pairs[i].loser]=true;
            }
        }


    return;
}

// Print the winner of the election
void print_winner(void)
{

  for(int i=0;i<candidate_count;i++)
  {
    int licznik=0;

      for(int j=0;j<candidate_count;j++)
      {
          if(locked[j][i]==false)//zliczaj ile razy jest false ponieważ wygrany ma kolumnę samych false
          {
            licznik++;
          }
      }
   if(licznik==candidate_count)
   {
    printf("%s\n",candidates[i]);
   }

  }
    return;
}
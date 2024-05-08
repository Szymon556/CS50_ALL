// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{

    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file
    typedef uint8_t BYTE;//tworzymy własny typ danych który będzie przechowywał jeden bajt czyli 8 bitó
    BYTE input_header[HEADER_SIZE];//tworzymy tablice która będzie przechowywała 44 bajtów

    size_t control=fread(input_header,HEADER_SIZE,1,input);//zapisujemy nagłowek z pliku input do tablicy input_header

    if(control!=1)//sprawdzamy czy fread zwraca tyle bajtów ile wynosi nagłowek jeśli nie to wyświetl w pliku błąd
    {
        fprintf(stderr, "fread() failed: %zu\n", control);
        exit(EXIT_FAILURE);
    }
    control=fwrite(input_header,HEADER_SIZE,1,output);//zapisujemy z tablicy nagłowek w pliku output

    if(control!=1)
    {
        fprintf(stderr, "fwrite() failed: %zu\n", control);
        exit(EXIT_FAILURE);
    }
    // TODO: Read samples from input file and write updated data to output file
    typedef int16_t BYTE16;
    BYTE16 buffor;


        while(fread(&buffor,sizeof(BYTE16),1,input))//w przypadku braku danych fread zrwaca 0 debilu czyli pętla się przerwie
        {
            buffor*=factor;
            fwrite(&buffor,sizeof(BYTE16),1,output);
        }






    // Close files
    fclose(input);
    fclose(output);
}

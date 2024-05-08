#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    string key;
    char buffor;
    char tab[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

   if(argc==2)//sprawdzamy czy mamy podany klucz i nic ponad to
   {
     key=argv[1];

     if(strlen(key)!=26)//sprawdzamy długość klucza
     {
        printf("Key must contain 26 characters.\n");

        return 1;
     }

   }else{//jeżeli podamy więcej niż dwa lub mniej argumentów to wypisze ten komunikat

    printf("Usage: ./substitution key\n");

    return 1;

   }

 for(int i=0, n=strlen(key);i<n;i++)//sprawdzamy czy żaden znak się nie powtarza
 {
    buffor = key[i];

   if(buffor<65||(buffor>90&&buffor<97)||buffor>122)
    {
      return 1;
    }

    for(int j=0, k=strlen(key);j<k;j++)
    {
      if(j!=i)
       {
            if(buffor==key[j])
            {
                printf("Key must not contain repeat characters\n");

                return 1;
            }
      }

    }
 }
      string plain_text = get_string("plaintext: ");

      int length = strlen(plain_text),counter=0,i=0;

      while(length!=counter)
      {
         buffor=plain_text[counter];

         if(isalpha(buffor))//sprawdzamy czy jest to znak alfanumryczny bo tylko dla takich dokonujemy podmiany
         {
            if(islower(buffor))//sprawdzamy czy jest mała litera
            {

            while(buffor!=tab[i])//powtarzaj tak długo aż nie znajdziesz danej litery

            {
               i++;
            }
               plain_text[counter]=tolower((unsigned char)key[i]);

            }else
            {



               while(tolower(buffor)!=tab[i])
               {
                  i++;
               }

                plain_text[counter]=toupper((unsigned char)key[i]);

            }

         }



         counter++;
         i=0;
      }



printf("ciphertext: %s\n", plain_text);

return 0;

}
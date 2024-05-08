#include <cs50.h>
#include <stdio.h>


int main(void)
{
int size,width,pointer,x=1;
//Entere the size
do{
    size = get_int("Enter the size: ");
}while(size<=0||size>=9);
width = size+3;
pointer = 0;
for(int i = 0; i<size;i++)
{
    for(int j=0;j<width;j++)
    {
       if(pointer<size-x)
       {
            printf(" ");

       }else if(pointer<size||pointer>=size+2)
       {
          printf("#");
       }else if (pointer>=size||pointer>size+2)
       {
             printf(" ");
       }
       pointer++;
    }
printf("\n");
width++;
x++;
pointer=0;
}



}
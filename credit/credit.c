#include <cs50.h>
#include <stdio.h>

int main(void)
{
     long int number,checksum=0,length=0,digit=0,sum=0,buffor=0,number_buffer;

    number= get_long("Enter the number: ");
    number_buffer = number;

 while(number>0)//Pętla działa tak długa aż przejedziemy cały łańcuch liczb i wyliczmy w niej sumę kontrolną
    {
        checksum = checksum + number%10;
        number=number/10;//odrzucamy ostatniąiczbą
        digit=number%10;//Przed ostatnią zapisujemy do sobnej zmiennej i mnożymy ją razy 2
        digit = digit*2;

            if(digit >=10)//ponieważ w algorytmie Luhna dodajemy pojedyncze cydry wiec jak wyjdzie np 12 to trzeba to rozbić na 1+2
            {

               buffor=buffor+digit%10;
               digit = digit/10;
               buffor=buffor+digit%10;
               digit = buffor;
               buffor=0;
             }
        sum=sum+digit;
        number=number/10;

    }
  number = number_buffer;
    while(number>0)//sprawdzamy dlugosc liczby
    {
       number=number/10;
       length++;

    }
     
    checksum = checksum+sum;
    sum=0;
    digit=0;
    buffor=0;
    int counter=1;
    for(int i = 0;i<length;i++)//szuakmy pierwszych 2 cyfr
    {
      number_buffer=number_buffer/10;
      if(counter == length-2)
      {
        digit=digit+number_buffer%10;

      }else if(counter == length-1)
      {

        buffor=buffor+number_buffer;
         digit=(buffor*10)+digit;


      }
      counter++;
    }


        if(length == 15&&(digit==37||digit==34)&&(checksum%10==0))
        {
           printf("AMEX\n");

        }else if(length == 16&&(digit==51||digit==52||digit==53||digit==54||digit==55)&&(checksum%10==0))
        {
          printf("MASTERCARD\n");

        }else if((length>=13&&length<=16)&&(digit/10==4)&&(checksum%10==0))
        {
             printf("VISA\n");
        }else{
            printf("INVALID\n");
        }




}


#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main()
{
   int game_tab[9][9];
   char spacer1[42] = "++===+===+===++===+===+===++===+===+===++";
   char spacer2[42] = "++---+---+---++---+---+---++---+---+---++";
   printf("%s",&spacer1);
   for(int i=0; i<9; i++){
     for(int j=0; j<9; j++){
       game_tab[i][j]=0;
       printf("%d",game_tab[i][j]);
     };
   if ((i+1) %% 3) == 0{
      printf("%s",&spacer2);
    };
  };
   return 0;
}

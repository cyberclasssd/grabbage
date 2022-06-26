#include <stdio.h>

int main(void) {
   char buffer[30];  

   gets(buffer);
 
   printf(buffer);
   return 0;
}

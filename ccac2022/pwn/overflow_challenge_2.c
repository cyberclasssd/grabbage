
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

void flag() {
  char buf[64];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag file is missing! You might be running this locally. If this happens on the remote server, please contact the teacher.");
    exit(0);
  }

  fgets(buf,64,f);
  printf(buf);
}

void vuln() {
	char buf[32];
	puts("Welcome to your first pwn challenge!");
	printf("What's your name?  ");
	gets(buf);
	printf("Hi, ", buf);
}

int main() {
	setbuf(stdout, NULL);
	gid_t gid = getegid();
	setresgid(gid,gid,gid);
	vuln();
	return 0;	
}

#include <stdio.h>

int main() {
  char s[100001];
  int t[100000],i,j,n;
  int M= 1000000000;
  int p[100001][3];
  int noll=0;
  scanf("%s", s);
  for(n=0;s[n];n++) t[n]=s[n]-'0'; 
  p[0][0]=p[0][1]=p[0][2]=0;
  for(i=0;i<n;i++) {
    for(j=0;j<3;j++) p[i+1][j]=p[i][j];
    for(j=0;j<3;j++) p[i+1][(j+t[i])%3]=(p[i+1][(j+t[i])%3]+p[i][j])%M;
    if(t[i]>0) p[i+1][t[i]%3]=(p[i+1][t[i]%3]+1)%M;
    else noll++;
  }
  printf("%d\n", (p[n][0]+noll)%M);
  return 0;
}

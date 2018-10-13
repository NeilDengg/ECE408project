#include <openssl/md5.h>
#include <iostream>
#include <cstdio>
#include <iomanip>
#include <string.h>
#include <stdlib.h>
#include <time.h>
using namespace std;

int main(){
	MD5_CTX c;
	unsigned char md5[16]={0};
	unsigned int  md5_len;
	int i=0;
	int r1,r2,r3,r4;
	char* str;
	char* match;
	char* result;
	/*const char* a="ffifdyop";*/
	srand(time(0));
	while(1){
	i++;
	r1=rand();r2=rand();r3=rand();r4=rand();
	sprintf(str,"%d%d%d%d",r1,r2,r3,r4);
	/*sprintf(str,"%s",a);*/
	MD5_Init(&c);
	MD5_Update(&c,str,strlen(str));
	MD5_Final(md5,&c);
	result =(char*) md5;
	match=strstr(result,"'||'");
	if(i%100000==0){
	cout<<i<<endl;}
	if(match==NULL)
		match=strcasestr(result,"'or'");
	if(match!=NULL && match[4]>'0' && match[4]<='9'){
	cout<<"content:"<<str<<endl;
	cout<<"count:"<<i<<endl;
	cout<<"hex:"<<md5;
	break;
}
	
}
	return 0;
}

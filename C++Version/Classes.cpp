#include <iostream>
#include <sys/socket.h>
#include <errno.h>
#include <stdlib.h>


void error (const char *msg)
{
    perror(msg);
    exit(0);
}



class fileTrans
{
  int sock = socket(AF_INET,SOCK_STREAM);

}

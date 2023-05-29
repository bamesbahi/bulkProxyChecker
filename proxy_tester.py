import os
import multiprocessing
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
from time import process_time_ns
from traceback import print_tb
import requests


def proxy_checker(ips):  
     ip=str(ips).split(':')[0]
     port=str(ips).split(':')[1]
     try:        
         url='https://mylocation.org/'

         proxies = {
             'http': 'http://'+ip+':'+port, 
             'https': 'http://'+ip+':'+port,
             }  
             
         response = requests.get(url, proxies=proxies)
         ping=response.elapsed.total_seconds()
         if str(ip) in str(response.content):
               
             if ping<0.9:
                 print(bcolors.BOLD+ip+bcolors.ENDC+" ==> "+bcolors.OKCYAN+"UP"+bcolors.ENDC+' --> '+bcolors.OKGREEN+str(ping)+bcolors.ENDC+'/sec  '+bcolors.BOLD+'(Fast)'+bcolors.ENDC)
                 f = open("./Proxies/fast.txt", "a")
                 f.writelines(ips+'\n')
                 f.close()
                 
             elif ping>1 and ping<1.8:
                 print(bcolors.BOLD+ip+bcolors.ENDC+" ==> "+bcolors.OKCYAN+"UP"+bcolors.ENDC+' --> '+bcolors.OKBLUE+str(ping)+bcolors.ENDC+'/sec')
                 m = open("./Proxies/medium.txt", "a")
                 m.writelines(ips+'\n')
                 m.close()
             elif ping >1.9:
                 print(bcolors.BOLD+ip+bcolors.ENDC+" ==> "+bcolors.OKCYAN+"UP"+bcolors.ENDC+' --> '+bcolors.WARNING+str(ping)+bcolors.ENDC+'/sec  (Very Slow)')
                 s = open("./Proxies/slow.txt", "a")
                 s.writelines(ips+'\n')
                 s.close()
                 
             
     except:
         print(bcolors.BOLD+ip+bcolors.ENDC+' ==> '+bcolors.FAIL+'Down'+bcolors.ENDC)
         s = open("./Proxies/DOWN.txt", "a")
         s.writelines(ips+'\n')
         s.close()









if __name__ == '__main__':
     os.system('cls')
     jobs=[]
     print(bcolors.UNDERLINE+'Please Wait...'+bcolors.ENDC)
     fileObject = open("./proxies.txt", "r")
     data = fileObject.read()
     d=data.split('\n')
     ip=0
     global err_proxies
     while ip<len(d):
         p1 = multiprocessing.Process(name='proxy_checker',target=proxy_checker, args=(d[ip],))
         #jobs.append(p1)
         p1.start()
         ip=ip+1
         
         time.sleep(0.3)
         
     time.sleep(3)
     print('Done')

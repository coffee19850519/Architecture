#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Fei --<>
  Purpose: test multiprocess
  Created: 2015/11/4
  Updated: 
"""

import unittest
from Download import Download
import threading
from multiprocessing.dummy import Pool as ThreadPool
import random
from time import sleep 
import argparse,ConfigDealer
          
#----------------------------------------------------------------------
class ExcuteCommand(threading.Thread):
    __command = '';
    def __init__(self, command):
        super(ExcuteCommand,self).__init__();
        self.__command = command;
        self.setDaemon(True);     

    def run(self): 
        pool = ThreadPool();
        jobs = [];
        if self.__command == 'download':
            for i in range(4):        
                d = Download(i,random.randint(1, 10));
                pool.apply_async(d.run);
                jobs.append(d);
        elif self.__command == 'p':
            print('sparse');
        elif self.__command == 'update':
            print('update DB'); 
        elif self.__command == 'stop':
            for job in jobs:
                job.join();
             
        else:
            pool.close();            
            pool.join();
            
                   
   
   
def DownloadSleep(interval):
    
    print('sub-process start');
    sleep(interval);
    print('sub-process complete');    
    
           

if __name__ == '__main__':
    
     #construct the usage
    description = 'usage: %prog arg1 arg2 arg3'
    parser = argparse.ArgumentParser(description = description)

    parser.add_argument('operator', nargs = '?', help = "The operation to execute")
    parser.add_argument('database', nargs = '?', help = "The database to operate")
    parser.add_argument('filePath', nargs = '*', help = "The filePath of configration.Default is ./config.cfg", default = 'config.cfg')

    #parse the input arguments
    args = parser.parse_args();
    #print (args.operator)
    
    cfgDealer = ConfigDealer.ConfigDealer(args.filePath)
    cfgDealer.excutebyConfig(args)    

    
from time import sleep
import multiprocessing


class Download(multiprocessing.Process):
    
       def __init__(self, num, interval):
              multiprocessing.Process.__init__(self)
              self.__interval = interval
              self.__num = num
              #self.setDaemon(True);     
    
       def run(self):
              #initial a series of sub-processing to 'Download' simultaneously
              print('#' + str(self.__num) + ' sub-process start')
              # do sth. to take time
              sleep(self.__interval)
              print('#' + str(self.__num) + ' sub-process complete in ' + str(self.__interval) + ' seconds')
    
    
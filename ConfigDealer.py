import configparser,os

class ConfigDealer:
    cfg = configparser.SafeConfigParser()
    
 #----------------------------------------------------------------------
    def __init__(self,fileName = 'config.cfg'):
        """Constructor"""
        
        #Open the configuration file and try to parse it
        try:
            with open(fileName, 'r', encoding='utf-8') as fh:
                try:
                    self.cfg.readfp(fh)
                except configparser.Error:
                    print(traceback.format_exc())     
        except IOError:
            print('Error: Could not read from config file')
      
      
    #----------------------------------------------------------------------
    def argsValidate(self,args):
        """
        All argument check can be collected here 
        
        """
        #check whether the database name is in config list
        if  (self.cfg.has_section(args.database) != True):
            return False
        
        else:
            return True
           
    
    #----------------------------------------------------------------------
    def  excutebyConfig(self, args):
        """"""
        #The operations in every section shall be executed in sequence
        if self.argsValidate(args) != True:
            raise Exception("Please check the command parameters and config file")
          
        #1st : Download     
        #Load the Downloader Model        
       
        moduleName,ext = os.path.splitext(os.path.basename(self.cfg.get(args.database, 'downloader path')))
        module = __import__(moduleName)                   
        # create an instance of downloader and invoke 'downloader'
        objectInstance = getattr(module, self.cfg.get(args.database, 'downloader'))(self.cfg.getint(args.database, 'thread'),self.cfg.getint(args.database, 'interval'))
        getattr(objectInstance,self.cfg.get(args.database, 'download function') )()
        
        
        #2nd : Parse
            
        #3rd : Storagy        
        
        '''
        sections = self.cfg.sections()
        for sec in sections:
            #The operations in every section shall be executed in sequence
            
            #1st : Download
            #Load the Downloader Model
            print(self.cfg.get(sec, 'url'))
            moduleName,ext = os.path.splitext(os.path.basename(self.cfg.get(sec, 'downloader path')))
           
            module = __import__(moduleName)
            
            # create an instance of downloader and invoke 'downloader'
            objectInstance = getattr(module, self.cfg.get(sec, 'downloader'))()
            getattr(objectInstance,self.cfg.get(sec, 'download function') )(self.cfg.get(sec, 'parameters'));
            

            
            
            #2nd : Parse
            
            
            #3rd : Storagy
                    #eval(item)
           '''
         
if __name__=="__main__": 
    cfgDealer = ConfigDealer()
    cfgDealer.excutebyConfig()
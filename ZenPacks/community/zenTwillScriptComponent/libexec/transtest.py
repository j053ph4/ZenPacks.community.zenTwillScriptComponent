#!/usr/bin/env python
import Globals
from optparse import OptionParser
from Products.ZenUtils.ZenScriptBase import ZenScriptBase
import os, sys, time, subprocess,re

class TwillScriptRun(ZenScriptBase):
    """
    """
    def __init__(self):
        """
        """
        ZenScriptBase.__init__(self, connect=False)
        self.status = 0
        
    def buildOptions(self):
        """
        """
        ZenScriptBase.buildOptions(self)
        self.parser.add_option('--name', dest='name',
            help='Friendly name for test')
        self.parser.add_option('--url', dest='url',
            help='URL for Twill script')
        self.parser.add_option('--script', dest='script',
            help='script contents')
        
    def run(self):
        """
        """
        lines = self.options.script.split('\\n')
        self.filename = self.options.name + "_" + self.options.url + ".tmp"
        self.filename = re.sub('[^A-Za-z0-9]+', '', self.filename)
        self.script = TwillScript(filename=self.filename, lines=lines)
        self.script.createFile()
        self.command = "twill-sh -q -u "+self.options.url+" "+self.script.filename
        self.start = time.time()
        self.status = subprocess.call(self.command, shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
        self.finish = time.time() - self.start

        if self.status == 0:
            print  "WEB TRANSACTION SUCCESSFUL|time="'%4.2lf'%self.finish+";;;0.00"
            sys.exit(0)
        else:
            print  "WEB TRANSACTION FAILED|time="'%4.2lf'%self.finish+";;;0.00"
            sys.exit(2)
        self.script.deleteFile()
        

class TwillScript:
    """
    """
    def __init__(self,filename='tempfile',tempdir='/tmp',lines=[]):
        self.tempdir = tempdir
        self.filename = self.tempdir+'/'+filename
        self.lines = lines

    def createFile(self):
        """
        """
        self.file = open(self.filename,'w')
        for l in self.lines:
            self.file.write(l+'\n')

    def deleteFile(self):
        """
        """
        remove(self.file)
     


if __name__ == "__main__":
    u = TwillScriptRun()
    u.run()    

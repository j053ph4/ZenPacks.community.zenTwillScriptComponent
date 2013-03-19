from ZenPacks.community.ConstructionKit.Construct import *
from Products.ZenModel.migrate.Migrate import Version
import os

class Definition():
    """
    """
    version = Version(2, 0, 0)
    zenpackroot = "ZenPacks.community" # ZenPack Root
    zenpackbase = "zenTwillScriptComponent" # ZenaPack Name

    #dictionary of components
    component = 'TwillScript'
    componentData = {
                  'singular': 'Web Transaction',
                  'plural': 'Web Transactions',
                  'displayed': 'alias', # component field in Event Console
                  'primaryKey': 'alias',
                  'properties': { 
                        'alias' : addProperty('Alias','Basic', switch='--name',optional='false'),
                        'url' : addProperty('URL','Basic', switch='--url',optional='false'),
                        'script': addProperty('Script','Basic',ptype='lines', switch='--script',optional='false'),
                        },
                  }
    packZProperties = []
    #dictionary of datasources
    createDS = True
    cmdFile = 'transtest.py'
    provided = True
    cycleTime = 300
    timeout = 60
    datapoints = ['time']
    # do not change below
    cwd = os.path.dirname(os.path.realpath(__file__)) # ZenPack files directory      
                            

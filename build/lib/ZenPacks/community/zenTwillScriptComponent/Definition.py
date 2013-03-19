from ZenPacks.community.ConstructionKit.Construct import *
from Products.ZenModel.migrate.Migrate import Version
import os

class Definition():
    """
    """
    version = Version(2, 0, 0)
    zenpackroot = "ZenPacks.community" # ZenPack Root
    zenpackbase = "zenTwillScriptComponent" # ZenaPack Name
    cwd = os.path.dirname(os.path.realpath(__file__)) # ZenPack files directory
    #dictionary of components
    component = 'TwillScript'
    cmdFile = 'transtest.py'
    componentData = {
                  'singular': 'Web Transaction',
                  'plural': 'Web Transactions',
                  'displayed': 'component', # component field in Event Console
                  'primaryKey': 'component',
                  'properties': { 
                        # Basic settings
                        'component' : addProperty('Alias','Basic', switch='--name',optional='false'),
                        'url' : addProperty('URL','Basic', switch='--url',optional='false'),
                        'script': addProperty('Arguments','Basic',ptype='lines', switch='--script',optional='false'),
                        },
                  }
    
    #dictionary of datasources
    datasource = component + 'DataSource'
    datasourceData = {}
    datasourceData['properties'] = {}
    datasourceData['properties'].update(componentData['properties'])
    datasourceData['properties']['timeout'] = addProperty('Timeout (s)','Timing',60,switch='-t')
    datasourceData['properties']['cycletime'] = addProperty('Cycle Time (s)','Timing',300,'int')
    datapoints = ['time']                  
                            

from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

TwillScriptDefinition = type('TwillScriptDefinition', (BasicDefinition,), {
        'version' : Version(2, 1, 1),
        'zenpackbase': "zenTwillScriptComponent",
        'component' : 'TwillScript',
        'componentData' : {
                          'singular': 'Web Transaction',
                          'plural': 'Web Transactions',
                          'displayed': 'alias', # component field in Event Console
                          'primaryKey': 'alias',
                          'properties': {
                                        'alias' : addProperty('Alias','Basic', switch='--name',optional='false'),
                                        'url' : addProperty('URL','Basic', switch='--url',optional='false'),
                                        'script': addProperty('Script','Basic',ptype='lines', switch='--script',optional='false'),
                                        'eventClass' : getEventClass('/WWW'),
                                        'productKey' : getProductClass('WWW'),
                                        },
                          },
        'createDS' : True,
        'addManual' : True,
        'cmdFile' : 'transtest.py',
        'datapoints' : ['time'],
        'saveOld': True,
        'loadOld': True,
        }
)

                            

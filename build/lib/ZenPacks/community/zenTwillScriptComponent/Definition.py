from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

DATA = {
        'version' : Version(2, 0, 0),
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
                                        },
                          },
        'createDS' : True,
        'addManual' : True,
        'cmdFile' : 'transtest.py',
        'datapoints' : ['time']
        }

TwillScriptDefinition = type('TwillScriptDefinition', (BasicDefinition,), DATA)

                            

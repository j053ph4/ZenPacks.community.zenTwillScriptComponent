from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from ZenPacks.community.zenTwillScriptComponent.interfaces import *

'''
args:  zenpack,compInfo,compInterface,infoProperties
'''

class TwillScriptInfo(ComponentInfo):
    implements( ITwillScriptInfo )
    url = ProxyProperty('url')
    alias = ProxyProperty('alias')
    script = ProxyProperty('script')


'''
args : zenpackname,zenpackname,dsclass,dsvolcclass,dsvolcvar,dsinfo,dsinterface,dsinfoproperties
'''
# datasource info
from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from zope.schema.vocabulary import SimpleVocabulary
from Products.Zuul.infos.template import RRDDataSourceInfo
from ZenPacks.community.zenTwillScriptComponent.interfaces import *
from ZenPacks.community.zenTwillScriptComponent.datasources.TwillScriptDataSource import *

def TwillScriptRedirectVocabulary(context):
    return SimpleVocabulary.fromValues(TwillScriptDataSource.onRedirectOptions)

class TwillScriptDataSourceInfo(RRDDataSourceInfo):
    implements(ITwillScriptDataSourceInfo)
    url = ProxyProperty('url')
    alias = ProxyProperty('alias')
    cycletime = ProxyProperty('cycletime')
    timeout = ProxyProperty('timeout')
    script = ProxyProperty('script')

    @property
    def testable(self):
        ''''''
        return False


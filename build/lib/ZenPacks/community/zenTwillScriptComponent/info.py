from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from ZenPacks.community.zenTwillScriptComponent.interfaces import ITwillScriptInfo,ITwillScriptDataSourceInfo
from Products.Zuul.infos import InfoBase

class TwillScriptInfo(ComponentInfo):
    """
    Info adapter for TwillScript components.
    """
    implements(ITwillScriptInfo)
    twillComponent = ProxyProperty("twillComponent")
    twillURL = ProxyProperty("twillURL")
    twillScript =  ProxyProperty("twillScript")
    
class TwillScriptDataSourceInfo(InfoBase):
    """
    Info adapter for TwillScript data source.
    """
    implements(ITwillScriptDataSourceInfo)
    enabled = ProxyProperty('enabled')
    eventKey = ProxyProperty('eventKey')
    timeout = ProxyProperty('timeout')
    
    @property
    def testable(self):
        """
        We can NOT test this datsource against a specific device
        """
        return False


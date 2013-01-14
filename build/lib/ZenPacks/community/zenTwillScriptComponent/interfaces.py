from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.interfaces import IFacade
from Products.Zuul.interfaces import IInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

class ITwillScriptInfo(IComponentInfo):
    """
    Info adapter for TwillScript components.
    """
    twillComponent = schema.Text(title=u"Component")
    twillURL = schema.Text(title=u"URL")
    twillScript = schema.List(title=u"Script")

class ITwillScriptDataSourceInfo(IInfo):
    """
    Info adapter for TwillScript data source.
    """
    enabled = schema.Bool(title=_t(u"Enabled"))
    eventKey = schema.Text(title=_t(u"Event Key"))
    timeout = schema.Int(title=_t(u"Timeout (seconds)"))
    
class IzenTwillScriptFacade(IFacade):
    
    def addTwillScript(self, ob, name, url, script):
        """  add Twill Script Component to device
        """
        

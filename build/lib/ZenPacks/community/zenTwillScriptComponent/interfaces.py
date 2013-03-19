
'''
args: componentInterface,comopnentInterfaceproperties,componentIFacade,iFacadeMethodName
'''

from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.interfaces import IFacade

from Products.Zuul.utils import ZuulMessageFactory as _t

from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version
if Version.parse('Zenoss ' + ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine


class ITwillScriptInfo(IComponentInfo):
    url = SingleLineText(title=_t(u'URL'))
    alias = SingleLineText(title=_t(u'Alias'))
    script = MultiLineText(title=_t(u'Script'))



class IzenTwillScriptComponentFacade(IFacade):
    def addTwillScript(self, ob, **kwargs):
        ''''''

'''
args : dsinterface,dsinterfaceproperties
'''

# datasource interface
from Products.Zuul.interfaces import IRRDDataSourceInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t

if Version.parse('Zenoss ' + ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine

class ITwillScriptDataSourceInfo(IRRDDataSourceInfo):
    url = SingleLineText(title=_t(u'URL'))
    alias = SingleLineText(title=_t(u'Alias'))
    cycletime = schema.Int(title=_t(u'Cycle Time (s)'))
    timeout = SingleLineText(title=_t(u'Timeout (s)'))
    script = MultiLineText(title=_t(u'Script'))



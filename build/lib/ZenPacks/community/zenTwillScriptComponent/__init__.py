import Globals
from Products.ZenModel.ZenPack import ZenPack as ZenPackBase
from Products.ZenUtils.Utils import unused
import os,re

from Products.CMFCore.DirectoryView import registerDirectory
skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

unused(Globals)
""" Add device relations
"""
from Products.ZenModel.OperatingSystem import OperatingSystem
from Products.ZenRelations.RelSchema import *
OperatingSystem._relations += (("twillComponents", ToManyCont(ToOne,
                                    "ZenPacks.community.zenTwillScriptComponent.TwillScript", "os")),
                            )

from Products.ZenUtils.Utils import monkeypatch,prepId

@monkeypatch('Products.ZenModel.Device.Device')
def manage_addTwillScript(self, name, url, script=[]):
    """make a Twill Script component"""
    from TwillScript import TwillScript
    id = prepId(name)
    component = TwillScript(id)
    self.os.twillComponents._setObject(component.id, component)
    component = self.os.twillComponents._getOb(component.id)
    component.twillComponent = name
    component.twillURL = url
    component.twillScript = script
    return component

class ZenPack(ZenPackBase):
    """ Twill Script Component
    """
    def install(self, app):
        ZenPackBase.install(self, app)
        for d in self.dmd.Devices.getSubDevices():
            d.os.buildRelations()

    def remove(self, app, leaveObjects=False):
        ZenPackBase.remove(self, app, leaveObjects)
        OperatingSystem._relations = tuple([x for x in OperatingSystem._relations if x[0] not in ('twillComponents')])
        for d in self.dmd.Devices.getSubDevices():
            d.os.buildRelations()

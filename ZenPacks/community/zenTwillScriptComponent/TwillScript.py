################################################################################
#
# This program is part of the zenTwillScriptComponent Zenpack for Zenoss.
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################
from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class TwillScript(OSComponent, ManagedEntity, ZenPackPersistence):

    """
    TwillScript contains the basic properties of a TwillScript component
    """
    portal_type = meta_type = 'TwillScript'
    
    twillComponent = ''
    twillURL = ''
    twillScript = ''

    _properties = (
        {'id':'twillComponent', 'type':'string', 'mode':''},
        {'id':'twillURL', 'type':'string', 'mode':''},
        {'id':'twillScript', 'type':'lines', 'mode':''},        
        )
    
    _relations = OSComponent._relations + (
        ("os", ToOne(ToManyCont, "Products.ZenModel.OperatingSystem", "twillComponents")),
        )
    
    isUserCreatedFlag = True
    def isUserCreated(self):
        """ required built-in
        """
        return self.isUserCreatedFlag
    
    def viewName(self):
        """ required built-in
        """
        return self.twillComponent
    titleOrId = name = viewName

    def primarySortKey(self):
        """ required built-in
        """
        return self.twillComponent
    
#    def getStatus(self):
#        """ required built-in
#        """
#        return self.statusMap()
#    
#    def statusMap(self):
#        """ map run state to zenoss status
#        """
#        self.status = 0
#        return self.status
#    


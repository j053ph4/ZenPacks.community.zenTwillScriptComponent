'''
args:  compFacade,compClass,facadeName,iFacadeName,facadeMethodName, createMethod, singular
'''

import os,re
import logging
log = logging.getLogger('zen.zenTwillScriptComponentFacade')

from zope.interface import implements
from Products.Zuul.facades import ZuulFacade
from Products.Zuul.utils import ZuulMessageFactory as _t
from TwillScript import *
from .interfaces import *

class zenTwillScriptComponentFacade(ZuulFacade):
    implements(IzenTwillScriptComponentFacade)
    
    def addTwillScript(self, ob, **kwargs):
    	target = ob
    
        from Products.ZenUtils.Utils import prepId
        from ZenPacks.community.zenTwillScriptComponent.TwillScript import TwillScript
        import re
        cid = ''
        for k,v in kwargs.iteritems():
            if type(v) != bool:
                cid += str(v)
        cid = re.sub('[^A-Za-z0-9]+', '_', cid)
        id = prepId(cid)
        component = TwillScript(id)
        relation = target.os.twillScripts
        relation._setObject(component.id, component)
        component = relation._getOb(component.id)
        for k,v in kwargs.iteritems():
            setattr(component,k,v) 
        
    
    
    

    	return True, _t("Added Web Transaction for device " + target.id)


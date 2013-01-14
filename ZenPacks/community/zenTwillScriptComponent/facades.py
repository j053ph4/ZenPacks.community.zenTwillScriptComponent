import os,re
import logging
log = logging.getLogger('zen.zenTwillScriptfacade')

from zope.interface import implements
from Products.Zuul.facades import ZuulFacade
from Products.Zuul.utils import ZuulMessageFactory as _t
from TwillScript import TwillScript
from .interfaces import IzenTwillScriptFacade


class zenTwillScriptFacade(ZuulFacade):
    implements(IzenTwillScriptFacade)

    def addTwillScript(self, ob, name='', url='', script=[]):
        """ Adds TwillScript Component"""
        id = ob.id + '_' + name
        component = TwillScript(id)
        ob.os.twillComponents._setObject(component.id, component)
        component = ob.os.twillComponents._getOb(component.id)
        component.twillComponent = name
        component.twillURL = url
        component.twillScript = script
        return True, _t(" Added Twill Script for device %s" % (ob.id))


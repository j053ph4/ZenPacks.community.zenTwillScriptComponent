from Products.ZenUtils.Ext import DirectRouter, DirectResponse
from Products import Zuul

class zenTwillScriptRouter(DirectRouter):
    def _getFacade(self):
        return Zuul.getFacade('zenTwillScriptAdapter', self.context)

    def addTwillScriptRouter(self, name, url, script):
        facade = self._getFacade()
        ob = self.context
        success, message = facade.addTwillScript(ob, name, url, script)
        if success:
            return DirectResponse.succeed(message)
        else:
            return DirectResponse.fail(message) 

from Products.ZenModel.BasicDataSource import BasicDataSource
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence

class TwillScriptDataSource(ZenPackPersistence, BasicDataSource):

    ZENPACKID = 'ZenPacks.community.zenTwillScriptComponent'

    TWILL = 'Twill'
    sourcetypes = (TWILL,)
    sourcetype = TWILL
    
    timeout = 60
    eventClass = '/App/Twill'
    component = "${here/twillComponent}"
    url = "${here/twillURL}"
    script = "${here/twillScript}"

    _properties = BasicDataSource._properties + (
        {'id': 'command', 'type': 'string'},
        )

    def getDescription(self):
        return self.component

    def useZenCommand(self):
        return True

    def getCommand(self, context):
        parts = ['transtest.py']
        if self.component:
            parts.append("--name \"%s\" " % self.component)
        if self.url:
            parts.append("--url \"%s\" " % self.url)
        if self.script:
            parts.append("--script \"%s\" " % self.script)
        return BasicDataSource.getCommand(self, context, ' '.join(parts))

    def checkCommandPrefix(self, context, cmd):
        return self.getZenPack(context).path('libexec', cmd)



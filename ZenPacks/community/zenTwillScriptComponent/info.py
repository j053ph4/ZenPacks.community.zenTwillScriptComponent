from ZenPacks.community.ConstructionKit.ClassHelper import *

def TwillScriptgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class TwillScriptInfo(ClassHelper.TwillScriptInfo):
    ''''''

from ZenPacks.community.zenTwillScriptComponent.datasources.TwillScriptDataSource import *
def TwillScriptRedirectVocabulary(context):
    return SimpleVocabulary.fromValues(TwillScriptDataSource.onRedirectOptions)

class TwillScriptDataSourceInfo(ClassHelper.TwillScriptDataSourceInfo):
    ''''''



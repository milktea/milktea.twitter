from collective.grok import gs
from milktea.twitter import MessageFactory as _

@gs.importstep(
    name=u'milktea.twitter', 
    title=_('milktea.twitter import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('milktea.twitter.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here

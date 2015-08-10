from five import grok
from zope.formlib import form
from zope import schema
from zope.interface import implements
from zope.component import getMultiAdapter
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget


grok.templatedir('templates')

class IContentNavigation(IPortletDataProvider):
    
    twitter_username = schema.TextLine(
            title = u"Add Twitter Username",
            description = u"Shows twitter timeline by user",
            required=False,
        )


class Assignment(base.Assignment):
    implements(IContentNavigation)
    
    
    def __init__(self, twitter_username=None):
        self.twitter_username = twitter_username
       
       
    @property
    def title(self):
        return "Add Milktea Twitter Portlet"
    

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('templates/milkteatwitterportlet.pt')
    def __init__(self, context, request, view, manager, data):
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager
        self.data = data
        
        
    def contents(self):
        return self.data

class AddForm(base.AddForm):
    form_fields = form.Fields(IContentNavigation)
    # form_fields['item_title'].custom_widget = WYSIWYGWidget
    label = u"Add Milktea Twitter Portlet"
    description = ''
    
    def create(self, data):
        assignment = Assignment()
        form.applyChanges(assignment, self.form_fields, data)
        return assignment

class EditForm(base.EditForm):
    form_fields = form.Fields(IContentNavigation)
    # form_fields['item_title'].custom_widget = WYSIWYGWidget
    label = u"Edit Milktea Twitter Portlet"
    description = ''

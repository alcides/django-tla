from datetime import timedelta
from elementtree.ElementTree import ElementTree
from urllib import urlopen

from django import template
from django.conf import settings


register = template.Library()


def tla_list(request):
    """
    """
    url = 'http://www.text-link-ads.com/xml.php?inventory_key=' + settings.TLA_INVENTORY_KEY + '&referer=' + request.META.get('REQUEST_URI', request.META.get('PATH_INFO', '/'))
    agent = '&user_agent=' + request.META['HTTP_USER_AGENT']
    links = get_xml(url+agent)
    
    return {
        'links': links
    }

def get_xml(url):
    tree = ElementTree.parse(urlopen(url))
    links = tree.getroot()
    return links

register.inclusion_tag('templates/tla_list.html')(tla_list)

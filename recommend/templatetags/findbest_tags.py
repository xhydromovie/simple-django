from django import template

register = template.Library()

@register.filter(name='multi')
def multi(value, arg):
    """ Return multipled value """
    return int(value * arg)

@register.filter()
def thumbnail(value):
    if len(value) > 5:
        video_id = value.split("=")
        thumbnail_url = "https://img.youtube.com/vi/{}/mqdefault.jpg".format(video_id[1])
        print(thumbnail_url)
        return thumbnail_url
    else:
        return 'error'

@register.filter(name='listed')
def listed(value):
    listy = value.split(',')
    print(listy)
    return listy
from django.conf import settings
import os.path


def getImage(denker):
    url = os.path.join(settings.STATIC_ROOT, 'denker/images', denker.slug) + ".jpg"
    if os.path.isfile(url):
        denker.image = denker.slug
        print(denker.slug + ' exists at static/denker/images' + denker.slug + '.jpg!')
    else:
        denker.image = "ma_logo"
        print('Could not find ' + url)
    return denker

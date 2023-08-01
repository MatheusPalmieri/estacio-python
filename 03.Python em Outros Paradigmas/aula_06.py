from functools import partial
user = {
    'name': "Matheus Palmieri",
    'social_medias': [
        {
            'name': 'Facebook',
            'image_profile': '',
            'image_background': 'imagem_01',
        },
        {
            'name': 'Instagram',
            'image_profile': 'imagem_02',
            'image_background': '',
        },
    ]
}


def get_image_profile(user):
    for social in user['social_medias']:
        if social[image_profile]:
            return social['image_profile']
    return 'default'


def get_image_background(user):
    for social in user['social_medias']:
        if social[image_background]:
            return social['image_background']
    return 'default'


def get_image(image, user):
    for social in user['social_medias']:
        if social[image]:
            return social[image]
    return 'default'


get_image_profile = partial(get_image, 'image_profile')
get_image_background = partial(get_image, 'image_background')

print(get_image_profile(user))
print(get_image_background(user))

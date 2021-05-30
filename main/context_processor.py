from main.models import GeneralInfo, InfoPages


def extras(request):
    general = GeneralInfo.objects.get(id=1)

    info_pages = InfoPages.objects.values('name')


    #UNCOMMENT IF CANNOT > GeneralInfo.objects.get(id=1)
    # general = {'name': 'da'}
    # info_pages = ['da']

    return {'general': general, 'info_pages': info_pages}


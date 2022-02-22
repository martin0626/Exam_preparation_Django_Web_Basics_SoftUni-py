from DjangoExamPrep02.Library.helpers import get_profile


def profile_processor(request):
    profile = get_profile()
    return {'profile': profile}
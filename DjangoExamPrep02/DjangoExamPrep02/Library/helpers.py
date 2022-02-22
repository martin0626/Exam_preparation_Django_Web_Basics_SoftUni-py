from DjangoExamPrep02.Library.models import Profile


def get_profile():
    return Profile.objects.first()

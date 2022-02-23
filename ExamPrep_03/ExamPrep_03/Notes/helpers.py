from ExamPrep_03.Notes.models import Profile


def get_profile():
    return Profile.objects.first()

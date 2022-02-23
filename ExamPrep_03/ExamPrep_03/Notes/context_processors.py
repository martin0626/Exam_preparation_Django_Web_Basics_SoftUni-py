from ExamPrep_03.Notes.helpers import get_profile


def profile_processor(request):
    profile = get_profile()
    return {'profile': profile}

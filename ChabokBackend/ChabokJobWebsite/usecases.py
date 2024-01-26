from .models import JobOffer


def get_jobOffer_by_id(id):
    return JobOffer.find_by_id(id)
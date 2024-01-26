from .models import JobOffer, User


def get_jobOffer_by_id(id):
    return JobOffer.find_by_id(id)

def create_job_offer(job_offer):
    jobOffer = JobOffer(**job_offer)
    jobOffer.save()
    return jobOffer

def find_jobOffers_by_user(user):
    return JobOffer.find_by_user(user)

def delete_job_offer(job_offer):
    job_offer.delete()
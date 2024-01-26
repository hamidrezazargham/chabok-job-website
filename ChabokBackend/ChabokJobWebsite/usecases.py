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
    
def update_job_offer(job_offer, jobOfferData):
    job_offer.title = jobOfferData['title']
    job_offer.company_name = jobOfferData['company_name']
    job_offer.location = jobOfferData['location']
    job_offer.type_collabration = jobOfferData['type_collabration']
    job_offer.job_description = jobOfferData['job_description']
    job_offer.reqired_skils = jobOfferData['reqired_skils']
    job_offer.company_description = jobOfferData['company_description']
    job_offer.save()
    return job_offer
from rest_framework import serializers
from .models import User, Application, JobOffer, Resume, Status, Role

    

class userInfoSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128, allow_blank=False)
    first_name = serializers.CharField(max_length=128, allow_blank=False)
    last_name = serializers.CharField(max_length=128, allow_blank=False)
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    role = serializers.SerializerMethodField("get_role")
    gender = serializers.SerializerMethodField("get_gender")
    age = serializers.IntegerField()
    image_url = serializers.ImageField(use_url=True)
    city = serializers.CharField(max_length=128)
    province = serializers.CharField(max_length=128)
    
    def get_role(self, obj):
        return obj.get_role()
    
    def get_gender(self, obj):
        return obj.get_gender()


class jobOfferSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256)
    company_name = serializers.CharField(max_length=128)
    location = serializers.CharField(max_length=128)
    type_collabration = serializers.CharField(max_length=128)
    job_description = serializers.CharField(max_length=512, null=True, blank=True)
    reqired_skils = serializers.CharField(max_length=512, null=True, blank=True)
    company_description = serializers.CharField(max_length=512, null=True, blank=True)
    author = serializers.SerializerMethodField("get_author")
    
    def get_author(self, obj):
        author = userInfoSerializer(obj.get_author())
        return author.data
    

class resumeSerializer(serializers.Serializer):
    file_url = serializers.FileField(allow_empty_file=False, use_url=True)


class applicationSerializer(serializers.Serializer):
    user = serializers.SerializerMethodField("get_user")
    resume = serializers.SerializerMethodField("get_resume")
    status = serializers.SerializerMethodField("get_status")
    job_offer = serializers.SerializerMethodField("get_jobOffer")
    
    def get_user(self, obj):
        user = userInfoSerializer(obj.get_user())
        return user.data
    
    def get_resume(self, obj):
        resume = resumeSerializer(obj.get_resume())
        return resume.data
    
    def get_status(self, obj):
        return obj.get_status()
    
    def get_jobOffer(self, obj):
        job_offer = jobOfferSerializer(obj.get_job_offer())
        return job_offer.data
    
    
class jobSeekerHomePageSerializer(serializers.Serializer):
    image_url = serializers.SerializerMethodField("get_image")
    applications = serializers.SerializerMethodField("get_applications")
    recomendations = serializers.SerializerMethodField("recommend")
    
    def get_image(self, obj):
        return obj.get_image()
    
    def get_applications(self, obj):
        applications = applicationSerializer(Application.find_by_user_id(obj.id), many=True)
        return applications.data
    
    def recommend(self, obj):
        job_offers = jobOfferSerializer(JobOffer.recommend_by_user(obj), many=True)
        return job_offers.data
    

class employerHomePageSerializer(serializers.Serializer):
    image_url = serializers.SerializerMethodField("get_image")
    job_offers = serializers.SerializerMethodField("get_jobOffers")
    
    def get_image(self, obj):
        return obj.get_image()
    
    def get_jobOffers(self, obj):
        job_offers = jobOfferSerializer(JobOffer.find_by_user(obj), many=True)
        return job_offers.data
    

class viewJobApplicantsSerializer(serializers.Serializer):
    job_offer = serializers.SerializerMethodField("get_jobOffer")
    applications = serializers.Serializer("get_applications")
    
    def get_jobOffer(self, obj):
        job_offer = jobOfferSerializer(obj)
        return job_offer.data
    
    def get_applications(self, obj):
        applications = applicationSerializer(Application.find_by_job_offer(obj), many=True)
        return applications.data


class viewJobsSerializer(serializers.Serializer):
    job_offer = serializers.SerializerMethodField("get_jobOffer")
    
    def get_jobOffer(self, obj):
        job_offer = jobOfferSerializer(obj)
        return job_offer.data
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.db.models import F


# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user.username/<filename>
    return 'profile/user_{0}/{1}'.format(instance.user.get().username, instance.user.get().username + "." + filename.split(".")[-1])
    
class Resume(models.Model):
    file_url = models.FileField(upload_to=user_directory_path, default=None, null=True)
    
class Gender(models.IntegerChoices):
    MALE = 0, _('MALE')
    FEMALE = 1, _('FEMALE')
    
class Role(models.IntegerChoices):
    EMPLOYER = 0, _('EMPLOYER')
    JOB_SEEKER = 1, _('JOB_SEEKER')
    
class Status(models.IntegerChoices):
    REJECTED = -1, _('REJECTED')
    WAITING = 0, _('WAITING')
    ACCEPTED = 1, _('ACCEPTED')


class UserInfo(models.Model):
    first_name = models.CharField(max_length=128, default='', null=True, blank=True)
    last_name = models.CharField(max_length=128, default='', null=True, blank=True)
    gender = models.IntegerField(
        choices=Gender.choices,
        default=None,
        null=True,
        blank=True
    )
    age = models.IntegerField(default=None, null=True)
    image = models.ImageField(upload_to=user_directory_path, default=None, null=True)
    province = models.CharField(max_length=128, default=None, null=True, blank=True)
    city = models.CharField(max_length=128, default=None, null=True, blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, related_name='user_info', default=None, null=True, blank=True)
    
    def get_image(self):
        if not self.image:
            return 'no-image'
        return self.image.url

class User(AbstractBaseUser):
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField()
    is_employer = models.IntegerField(
        choices=Role.choices,
        default=Role.JOB_SEEKER
    )
    user_info = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, related_name='user', default=None, null=True, blank=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username','email', 'is_employer']
    
    
    def __str__(self):
        return self.username
    
    def get_user_info(self):
        return User.objects.filter(id = self.id).values('id', 'username', 'email', 'user_info', role=Role(int(self.role)).name,
            first_name=F('user_info__first_name'), last_name=F('user_info__last_name'), gender=Gender(int(F('user_info__gender'))).name, age=F('user_info__age'), image=F('user_info__image'),
            province=F('user_info__province', city=F('user_info__city'))).first()
    
    def get_role(self):
        return Role(int(self.role)).name
    
    def get_gender(self):
        if self.gender != None:
            return Gender(int(self.gender)).name
        return self.gender
    
    @classmethod
    def find_by_id(cls, id):
        return cls.objects.get(id=id)
    
    @classmethod
    def find_by_username(cls, username):
        return cls.objects.get(username=username)
    
class JobOffer(models.Model):
    title = models.CharField(max_length=256)
    company_name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    type_collabration = models.CharField(max_length=128)
    job_description = models.CharField(max_length=512, null=True, blank=True)
    reqired_skils = models.CharField(max_length=512, null=True, blank=True)
    company_description = models.CharField(max_length=512, null=True, blank=True)
    
class Tag(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, related_name='tags', default=None, null=True)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.SET_NULL, related_name='tags', default=None, null=True)

class Application(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, related_name='applications')
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, related_name='applications')
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.WAITING
    )
    job_offer = models.ForeignKey(JobOffer, on_delete=models.SET_NULL, related_name='applications')
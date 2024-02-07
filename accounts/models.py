from django.contrib.auth.models import AbstractUser
from django.db import models
from base.models import Departement
from guardian.mixins import GuardianUserMixin
from simple_history.models import HistoricalRecords
from django.utils import timezone

class User(AbstractUser,GuardianUserMixin):
    contact = models.CharField(max_length=12)
    email = models.EmailField(unique=True, blank=True)
    departement =  models.ForeignKey(Departement,on_delete=models.CASCADE,default=1,related_name="users")
    last_password_change = models.DateField(null=True,blank=True)
    updated = models.DateTimeField(null=True,blank=True)

    reset_by_admin = models.BooleanField(default=False)
    history = HistoricalRecords() 
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    class Meta:
        verbose_name="Utilisateur"
        verbose_name_plural="Utilisateurs"
        default_permissions = ()
        
    def __str__(self):
        return self.username
    
    @property
    def age_of_last_password_change(self):
        if self.last_password_change:
            current_time = timezone.now().date()
     
            age = current_time - self.last_password_change
            
            return age.days

        return 0
        

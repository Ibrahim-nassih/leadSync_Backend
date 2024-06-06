from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone



class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    keycloak_user_id = models.CharField(max_length=255, null=True, blank=True)
    group_name=models.CharField(max_length=255, null=True, blank=True)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'firstName', 'lastName']

    def __str__(self):
        return self.username


class Space(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    privacy = models.CharField(max_length=255, default='public')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Other fields

class Workflow(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    # Other fields
class Step(models.Model):
    name = models.CharField(max_length=255)
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    # Other fields
class Transaction(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    from_step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='transactions_from')
    to_step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='transactions_to')
    created_at = models.DateTimeField(default=timezone.now)
class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(CustomUser, through='Membership')
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    # Other fields

class Membership(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    # Other fields
class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=20, default='Medium')
    ticket_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)   
    # Relationships
    status = models.ForeignKey(Step, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Membership, on_delete=models.PROTECT)
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    parent_ticket=models.IntegerField(null=True, blank=True)
    sprint=models.IntegerField(null=True, blank=True)
    estimationDurationMinutes=models.IntegerField(null=True, blank=True)

class Sprint(models.Model):
    name = models.CharField(max_length=100, verbose_name="Sprint Name")
    start_date = models.DateTimeField(verbose_name="Start Date")
    end_date = models.DateTimeField(verbose_name="End Date")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)


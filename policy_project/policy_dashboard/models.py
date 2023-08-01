from django.db import models

# model for policy 

class Policy(models.Model):
    POLICY_STATUS_CHOICES = (
        ('1', 'Requirements Awaited'),
        ('2', 'Requirements Closed'),
        ('3', 'Underwriting'),
        ('4', 'Policy Issued'),
        ('5', 'Policy Rejected'),
    )

    POLICY_MEDICAL_TYPE_CHOICES = (
        ('1', 'Tele Medicals'),
        ('2', 'Physical Medicals'),
    )

    POLICY_MEDICAL_STATUS_CHOICES = (
        ('1', 'Pending'),
        ('2', 'Scheduled'),
        ('3', 'Waiting for Report'),
        ('4', 'Done'),
    )

    application_number = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    policy_cover = models.DecimalField(max_digits=10, decimal_places=2)
    policy_status = models.CharField(choices=POLICY_STATUS_CHOICES, max_length=1)
    policy_number = models.CharField(max_length=100, blank=True, null=True)
    medical_type = models.CharField(choices=POLICY_MEDICAL_TYPE_CHOICES, max_length=1, blank=True, null=True)
    medical_status = models.CharField(choices=POLICY_MEDICAL_STATUS_CHOICES, max_length=1, blank=True, null=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.application_number


# models for comments 

class Comment(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment #{self.pk} for Policy #{self.policy.pk}'
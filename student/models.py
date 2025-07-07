from django.db import models


class Participant(models.Model):
    DISCIPLINARY_CASE_CHOICES = [
        ('basic_training', 'Basic Training'),
        ('bad_behavior', 'Bad Behavior'),
        ('rudeness', 'Rudeness'),
        ('bullying', 'Bullying'),
        ('cheating', 'Cheating'),
        ('vandalism', 'Vandalism'),
        ('truancy', 'Truancy'),
        ('disrespect_authority', 'Disrespect to Authority'),
        ('theft', 'Theft'),
        ('substance_abuse', 'Substance Abuse'),
        ('inappropriate_social_media', 'Inappropriate Social Media Use'),
        ('fighting', 'Fighting'),
        ('gambling', 'Gambling'),
        ('sexual_misconduct', 'Sexual Misconduct'),
        ('disruptive_behavior', 'Disruptive Behavior'),
        ('poor_attendance', 'Poor Attendance'),
        ('failure_to_follow_rules', 'Failure to Follow Rules'),
        ('other', 'Other'),
    ]
    
    
    GENDER_CHOICES = [
        ('female','FEMALE'),
        ('male','MALE')
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    date_of_birth = models.DateField()
    next_of_kin = models.CharField(max_length=50, blank=False)
    next_of_kin_number = models.CharField(max_length=50, blank=False)
    displinary_case = models.CharField(max_length=50, blank=False, choices=DISCIPLINARY_CASE_CHOICES , default='basic_training')
    gender  = models.CharField(max_length=50, blank=False, null=False, choices=GENDER_CHOICES, default='male')
    contact = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=150, blank=False)  
    email = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

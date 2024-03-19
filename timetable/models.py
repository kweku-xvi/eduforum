import uuid
from django.db import models


class Course(models.Model):
    COURSE_TYPE = [
        ('Theory', 'Theory'),
        ('Lab', 'Lab')
    ]

    course_code = models.CharField(max_length=20, primary_key=True, unique=True)
    course_name = models.CharField(max_length=100)
    course_type = models.CharField(max_length=20, choices=COURSE_TYPE)
    credit_hours = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.course_code} - {self.course_name}'

    
    class Meta:
        ordering = ('-created_at',)


class Lecturer(models.Model):
    lecturer_id = models.CharField(max_length=6, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    office_location = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.lecturer_id:
            self.lecturer_id = str(uuid.uuid4())[:6]
        super().save(*args, **kwargs)

    
    class Meta:
        ordering = ('-created_at',)


class Class(models.Model):
    CLASS_DAYS = [
        ('Monday', 'Mon'),
        ('Tuesday', 'Tue'),
        ('Wednesday', 'Wed'),
        ('Thursday', 'Thurs'),
        ('Friday', 'Fri'),
    ]

    class_id = models.CharField(primary_key=True, unique=True, max_length=13)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    week_day = models.CharField(max_length=20, choices=CLASS_DAYS)
    time_start = models.TimeField()
    time_end = models.TimeField()
    class_location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.week_day} - {self.course.course_name}'

    
    def save(self, *args, **kwargs):
        if not self.class_id:
            self.class_id = str(uuid.uuid4())[:13]
        super().save(*args, **kwargs)

    
    class Meta:
        ordering = ('-created_at',)
# 다 대 다 관계



New Project 생성

pip install --upgrade pip 업그레이드

pip install django 설치

pip install ipython 설치

pip install django_extentions 설치

django-admin startproject model_relation .   프로젝트 생성

model_relation - setting.py 코드 수정

```python
INSTALLED_APPS = [
    # 3rd party apps
    'django_extensions',
    
    # Django app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

python manage.py shell_plus 접속 확인

```
(venv) ➜  DjangoModelRelation python manage.py shell_plus
# Shell Plus Model Imports
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
from django.utils import timezone
from django.urls import reverse
Python 3.7.3 (default, Mar 27 2019, 09:23:15) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:     

exit
```



python manage.py startapp manytomany   앱 생성

model_relation - setting.py 코드 수정

```python
INSTALLED_APPS = [
    # local apps
    'manytomany',
    
    # 3rd party apps
    'django_extensions',

    # Django app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



manytomany.py - models.py 코드 수정

```python
from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}번 의사 {self.name}'


class Patient(models.Model):
    name = models.CharField(max_length=20)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}번 환자 {self.name}'


```



python manage.py makemigrations

python manage.py migrate

manytomany - models.py 코드 수정

```python
from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}번 의사 {self.name}'


class Patient(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}번 환자 {self.name}'


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'

```



db.sqlite3 삭제

기존 manytomany - migrations - 0001_initial.py 삭제

python manage.py makemigrations

python manage.py migrate

python manage.py shell_plus 접속 확인

```
# 의사 생성
In [1]: doctor = Doctor.objects.create(name='jason')                                                                                                                                                                                      

In [2]: doctor                                                                                                                                                                                                                            
Out[2]: <Doctor: 1번 의사 jason>


# 환자 생성
In [1]: patient = Patient.objects.create(name='tak')                                                                                                                                                                                      

In [2]: patient                                                                                                                                                                                                                           
Out[2]: <Patient: 1번 환자 tak>


# 관계 설정
Reservation.objects.create(doctor=doctor, patient=patient)

# 관계 확인
doctor.reservation_set.all()
patient.reservation_set.all()


In [00]: for reservation in doctor.reservation_set.all(): 
    ...:     print(reservation.patient.name) 
    ...:                                      



                             
```


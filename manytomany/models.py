from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}번 의사 {self.name}'


class Patient(models.Model):
    name = models.CharField(max_length=20)
    # reservation 을 거치지 않고 바로 처리 할 수 있도록 하는 로직
    doctors = models.ManyToManyField(
        Doctor,
        # through='Reservation',  # through='' <- 중계 이름의 모델을 적어준다.  patient.doctor.all()
        related_name='patients',  # doctor에 연결된 patient 바로 검색할 수 있게 하는 로직  doctor.patients.all()
    )

    def __str__(self):
        return f'{self.id}번 환자 {self.name}'


# Doctor & Patient 두 테이블을 중계하는 Reservation 테이블 생성
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'


# 기존에 doctor 와 patient 두개를 다대다로 연결하려면 reservation 테이블을 생성해야했다.
# 하지만 지금은 테이블을 안쓰고 patient 에 related_name='patients', 추가하여 연결하는 로직으로 변경했다.

# doctor.patients.add(patient)    의사의 환자를 추가할 때
# doctor.patients.all()           의사의 환자 확인
# doctor.patients.remove(patient) 의사의 환자 삭제
# 반대도 가능
# patient.doctors.add(doctor)
# patient.doctors.all()
# patient.doctors.remove(doctor)
#Hospital management System
class Patient:
    def __init__(self,patient_id,patient_name,age,gender,contact):  #*arg=can receive multiple values
       self.__patient_id = patient_id # __ is used to make data private
       self.__patient_name= patient_name
       self.__age = age
       self.__gender = gender
       self.__contact = contact    
    
    def get_patientDetails(self):
        return {
            'Patient_id': self.__patient_id,
            'Name': self.__patient_name,
            'Age': self.__age,
            'Gender': self.__gender,
            'Contact': self.__contact
        }

class doctor:
    def __init__(self,doctor_id,doctor_name,specialization):
        self.__doctor_id = doctor_id 
        self.__doctor_name = doctor_name
        self.__specialization =specialization
    def get_doctorDetails(self):
        return {
            'Doctor ID': self.__doctor_id,
            'Name': self.__doctor_name,
            'Specialization': self.__specialization
        }

class MedicalReport:
    def __init__(self):
        self.__records={}
    def AddRecord(self, patient,doctor,diagnosys,medications):
        self.__records[patient.get_patientDetails()['Patient_id']]= {
            'Patient': patient.get_patientDetails(),
            'Doctor': doctor.get_doctorDetails(),
            'Diagnosys': diagnosys,
            'Medication': medications
        }  
    def get_records(self):
        return self.__records
               

patient1=Patient(123,'Ravi',23,'Male','+918765654322')
patient2=Patient(124,'Mavi',34,'Female','+918985654322')
patient3=Patient(125,'Manu',27,'Male','+918769854322')
doctor1=doctor(234,'Ram','Cardiologist')
doctor2=doctor(235,'Shyam','Neurologist')
print(patient1.get_patientDetails())
print(patient2.get_patientDetails())
print(patient3.get_patientDetails())
print(doctor1.get_doctorDetails())
print(doctor2.get_doctorDetails())

record_reg=MedicalReport()
record_reg.AddRecord(patient1,doctor1,'Heart Problem','Asprin')

print(record_reg.get_records()[123]['Patient']['Name'])
#print(record_reg.get_records()[]['Patient_id']['Name'])
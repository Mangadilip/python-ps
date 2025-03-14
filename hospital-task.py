from datetime import datetime

class Patient:
    def __init__(self, name, age, gender, disease):
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease
        self.patient_id = f"P{datetime.now().strftime('%H%M%S')}"  
        self.assigned_doctor = None

    def book_appointment(self, doctor_name):
        doctor = Doctor.get_doctor_by_name(doctor_name)
        if doctor:
            self.assigned_doctor = doctor_name
            print(f"Appointment booked with Dr. {doctor_name}.")
        else:
            print("Doctor not found or unavailable.")

    def view_details(self):
        print("\nPatient Details:")
        print(f"ID: {self.patient_id} | Name: {self.name} | Age: {self.age} | Gender: {self.gender}")
        print(f"Disease: {self.disease}")
        if self.assigned_doctor:
            print(f"Assigned Doctor: Dr. {self.assigned_doctor}")
        else:
            print("No doctor assigned yet.")

class Doctor:
    doctors_list = []  

    def __init__(self, name, specialization, availability=True):
        self.name = name
        self.specialization = specialization
        self.availability = availability
        Doctor.doctors_list.append(self)

    @classmethod
    def add_doctor(cls, name, specialization, availability=True):
        new_doctor = cls(name, specialization, availability)
        print(f"Doctor {name} ({specialization}) added successfully.")

    @classmethod
    def display_doctors(cls):
        print("\nAvailable Doctors:")
        if not cls.doctors_list:
            print("No doctors available.")
        for doctor in cls.doctors_list:
            status = "Available" if doctor.availability else "Not Available"
            print(f"Dr. {doctor.name} - {doctor.specialization} ({status})")

    @classmethod
    def get_doctor_by_name(cls, name):
        for doctor in cls.doctors_list:
            if doctor.name.lower() == name.lower() and doctor.availability:
                return doctor
        return None

class Hospital:
    @staticmethod
    def hospital_policies():
        print("\nHospital Policies:")
        print("1. Visiting Hours: 9 AM - 5 PM")
        print("2. Emergency Contact: +1234567890")
        print("3. Wear a mask and sanitize your hands.")

    @staticmethod
    def is_hospital_open():
        current_hour = datetime.now().hour
        print("Hospital is OPEN." if 9 <= current_hour < 17 else "Hospital is CLOSED.")
  

Doctor.add_doctor("karthik", "Cardiologist")
Doctor.add_doctor("ajay", "Neurologist", availability=False)


Doctor.display_doctors()


patient1 = Patient("vinay", 30, "Male", "Flu")


patient1.book_appointment("karthik")  

patient1.view_details()


Hospital.hospital_policies() 


Hospital.is_hospital_open()

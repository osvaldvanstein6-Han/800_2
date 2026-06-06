# Week 5 - Activity 4

## Class Diagram for a Clinic System

## Project Description

This activity is a continuation of Week 5 Activity 3. The purpose of this task is to share the Class Diagram for a Clinic System and provide a brief description of how the design supports the clinic scenario.

The Clinic System allows patients to book appointments, pay booking fees, and order medication. The class diagram shows the main classes, attributes, methods, and relationships required to support these functions.

---

## Clinic System Scenario

In this clinic system, a patient can book an appointment with a doctor. Each appointment records the appointment date, time, reason, and status. After booking an appointment, the patient can pay the booking fee through the payment system.

The patient can also order medication from the clinic. Each medication order can contain multiple order items, and each order item refers to one medication. The system stores medication information such as name, price, stock quantity, and dosage details.

This scenario is reflected in the class diagram through the relationships between Patient, Doctor, Appointment, Payment, MedicationOrder, OrderItem, and Medication.

---

## Class Diagram

Clinic Class Diagram

---

## Classes in the Diagram

### Patient

The Patient class represents a clinic patient. It stores patient information and provides methods for booking appointments, paying booking fees, ordering medication, and viewing records.

### Doctor

The Doctor class represents a doctor in the clinic. It stores doctor information such as name, specialization, phone, and email. It also provides methods for viewing schedules and appointments.

### Appointment

The Appointment class represents a booking between a patient and a doctor. It stores appointment information such as date, time, reason, and status.

### Payment

The Payment class represents the payment for an appointment booking fee. It stores payment amount, payment method, payment date, payment status, and transaction reference.

### MedicationOrder

The MedicationOrder class represents a medication order made by a patient. It stores order date, order status, and total amount.

### OrderItem

The OrderItem class represents an individual item inside a medication order. It stores quantity, dosage instruction, unit price, and subtotal.

### Medication

The Medication class represents medicine available in the clinic. It stores medication name, description, unit price, stock quantity, and unit.

---

## Relationships

The class diagram includes the following relationships:

- One Patient can have many Appointments.
- One Doctor can have many Appointments.
- One Appointment has one Payment.
- One Patient can have many Medication Orders.
- One Medication Order can contain many Order Items.
- One Medication can be used in many Order Items.

These relationships align with the clinic scenario because they support appointment booking, booking fee payment, and medication ordering.

---

## Alignment with Project Scenario

The class diagram is aligned with the clinic system scenario in the following ways:

- The appointment booking requirement is represented by the Patient, Doctor, and Appointment classes.
- The booking fee payment requirement is represented by the Appointment and Payment classes.
- The medication ordering requirement is represented by the Patient, MedicationOrder, OrderItem, and Medication classes.
- The relationships and multiplicities show how patients, doctors, appointments, payments, and medication orders interact with each other.

---

## Design Style

The class names follow UML naming conventions using PascalCase.

Attributes and methods follow Python-style snake_case naming to keep the diagram consistent with possible Python implementation.

Return types use Python-friendly types such as int, str, float, datetime, list, and None.

---

## Files Included

- README.md
- clinic_class_diagram.png

---

## GitHub Repository

https://github.com/osvaldvanstein6-Han/800_2

---

## Author

Han


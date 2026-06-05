# Week 3 - Activity 2

## Finance Money Exchange Database Design

### Introduction

This project presents an Entity Relationship Diagram (ER Diagram) for a finance money exchange software application. The system is designed to manage customers, currencies, exchange rates, transactions, and employees involved in money exchange services.

The database contains five entities and demonstrates the relationships between them using primary keys (PK), foreign keys (FK), and one-to-many (1:M) relationships.

---

## ER Diagram

Money Exchange ER Diagram

---

## Database Entities

### 1. CUSTOMER

The CUSTOMER entity stores information about customers who use the money exchange service.

Attributes:

- customer_id (PK)
- first_name
- last_name
- birthday
- email
- address

---

### 2. TRANSACTION

The TRANSACTION entity stores records of money exchange transactions. It is the central entity of the system.

Attributes:

- transaction_id (PK)
- customer_id (FK)
- rate_id (FK)
- employee_id (FK)
- amount
- transaction_date

---

### 3. EXCHANGE_RATE

The EXCHANGE_RATE entity stores exchange rates used during transactions.

Attributes:

- rate_id (PK)
- currency_id (FK)
- exchange_rate
- buy_rate
- sell_rate

---

### 4. CURRENCY

The CURRENCY entity stores information about different currencies supported by the system.

Attributes:

- currency_id (PK)
- currency_code
- currency_name
- currency_country
- currency_symbol

Examples of currency codes include:

- NZD – New Zealand Dollar
- USD – United States Dollar
- AUD – Australian Dollar
- EUR – Euro

---

### 5. EMPLOYEE

The EMPLOYEE entity stores information about staff members who process customer transactions.

Attributes:

- employee_id (PK)
- first_name
- last_name
- email
- phone
- position

---

## Relationships

### CUSTOMER and TRANSACTION

Relationship:

- CUSTOMER (1) → (M) TRANSACTION

Explanation:

One customer can perform many transactions, but each transaction belongs to only one customer.

---

### EMPLOYEE and TRANSACTION

Relationship:

- EMPLOYEE (1) → (M) TRANSACTION

Explanation:

One employee can process many transactions, but each transaction is processed by one employee.

---

### EXCHANGE_RATE and TRANSACTION

Relationship:

- EXCHANGE_RATE (1) → (M) TRANSACTION

Explanation:

One exchange rate can be used in many transactions, but each transaction uses one exchange rate.

---

### CURRENCY and EXCHANGE_RATE

Relationship:

- CURRENCY (1) → (M) EXCHANGE_RATE

Explanation:

One currency can have multiple exchange rate records, but each exchange rate record belongs to one currency.

---

## Design Justification

This database design is suitable for a finance money exchange application because it separates customer information, transaction records, employee data, currency information, and exchange rates into different entities.

The use of primary keys ensures that each record is uniquely identified. Foreign keys establish relationships between entities and maintain data integrity. The design minimizes data duplication and improves database organization.

The TRANSACTION entity acts as the central component of the system, connecting customers, employees, and exchange rates.

---

## Technologies Used

- Draw.io (ER Diagram Design)
- Git
- GitHub

---

## Screenshot

![ER_diagram](<Screenshot 2026-06-05 at 7.14.55 PM.png>)

---

## Author

Han


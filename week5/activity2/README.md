# Week 5 - Activity 2

## Explanation of Figure 6.2 – Partial Use Case Context Diagram

---

# Introduction

This activity focuses on analyzing and explaining Figure 6.2 from the textbook Applying UML and Patterns: An Introduction to Object-Oriented Analysis and Design and the Unified Process. The diagram is a Partial Use Case Context Diagram that illustrates how users and external systems interact with the NextGen system.

The purpose of this activity is to understand the key elements of a UML Use Case Diagram and evaluate possible improvements to the design.

---

# Overview of Figure 6.2

Figure 6.2 presents a high-level view of the NextGen system. It shows:

- System Boundary
- Actors
- Use Cases
- Associations between actors and use cases

The diagram helps stakeholders understand who interacts with the system and what services the system provides.

---

# Explanation of Diagram Components

## 1. System Boundary

The large rectangle labeled NextGen represents the system boundary.

The system boundary defines the scope of the application and separates internal system functionality from external actors.

All use cases inside the rectangle belong to the NextGen system, while all actors remain outside the system boundary.

---

## 2. Actors

Actors are external entities that interact with the system.

### Cashier

The Cashier is the primary user of the system and performs daily business operations.

The Cashier interacts with:

- Process Sale
- Handle Returns
- Process Rental
- Cash In

---

### System Administrator

The System Administrator is responsible for system maintenance and security management.

The administrator interacts with:

- Manage Security
- Manage Users

---

### External System Actors

Several external systems also interact with NextGen:

- Payment Authorization Service
- Tax Calculator
- Accounting System
- HR System
- Sales Activity System

These systems exchange information with NextGen and support business operations.

For example:

- Payment Authorization Service validates payments.
- Tax Calculator calculates sales taxes.
- Accounting System records financial transactions.
- HR System provides employee-related information.
- Sales Activity System provides sales data for reporting and analysis.

---

## 3. Use Cases

Use cases represent services provided by the system.

### Process Sale

Allows a cashier to complete a sales transaction.

### Handle Returns

Processes returned products and customer refunds.

### Process Rental

Manages rental transactions.

### Cash In

Records cash deposits and cash balancing activities.

### Analyze Activity

Analyzes sales and business performance information.

### Manage Security

Allows administrators to configure security settings.

### Manage Users

Allows administrators to create, update, and manage user accounts.

---

## 4. Associations

Associations are represented by solid lines connecting actors and use cases.

These lines show communication between actors and the system functions.

Examples:

- Cashier → Process Sale
- Cashier → Handle Returns
- System Administrator → Manage Users
- Payment Authorization Service → Process Sale

---

# Purpose of the Diagram

The purpose of Figure 6.2 is to:

- Define the system scope.
- Identify system users.
- Identify external systems.
- Show major system functions.
- Provide a high-level overview of the application.

The diagram is useful during requirements analysis because it helps developers and stakeholders understand the system before implementation begins.

---

# Recommendations for Improvement

## Recommendation 1: Add Include and Extend Relationships

The diagram currently shows only actor-use case associations.

The model could be improved by adding UML relationships such as:

- <<include>>
- <<extend>>

For example, the Process Sale use case could include payment authorization and tax calculation activities. This would provide a more detailed representation of system behavior and use case dependencies.

---

## Recommendation 2: Organize Use Cases into Functional Groups

As systems become larger, diagrams can become difficult to read.

The use cases could be grouped into logical categories such as:

### Sales Management

- Process Sale
- Handle Returns
- Cash In

### Rental Management

- Process Rental

### System Administration

- Manage Security
- Manage Users

### Reporting and Analysis

- Analyze Activity

This would improve readability and make the diagram easier to maintain.

---

# Conclusion

Figure 6.2 effectively illustrates the interactions between users, external systems, and the NextGen application. It clearly defines the system boundary and identifies the major business functions provided by the system.

However, the diagram could be improved by adding include and extend relationships and organizing use cases into functional groups. These improvements would provide greater clarity and improve the overall design quality.

---

# Reference

Larman, C. (2005). Applying UML and Patterns: An Introduction to Object-Oriented Analysis and Design and the Unified Process (2nd Edition). Prentice Hall.

---

# Author

Han

MSE800 – Software Engineering

Week 5 Activity 2
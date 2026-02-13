---
layout: post
tags: [ "cst363", 'csumb']
title: "Pharmacy Database System"
description: "A database system and a robust backend solution for managing complex information."
project-title: "Pharmacy Database"
project-url: "/assets/docs/Lab 19 Web App JDBC.pdf"
image: "/assets/imgs/project/database.png"
status: completed
tools: [MySQL, JDBC, Java]
---


This database project for [CST363: Introduction to Database Management](/csumb/cst363/) focuses on the design and implementation of a relational system tailored for pharmacy operations. I architected a schema to support the complex relationships between patients, providers, and multi-location inventories.
<!--more-->
The project includes:

- **Entity Modeling**: Architected a schema around five core entities: Doctor, Patient, Drug, Pharmacy, and
  Prescription.
- **Relational Integrity**: Implemented junction tables such as `prescription_refill` to track medication history and
  refills.
- **Financial Tracking**: Developed a `drug_cost` module to manage dynamic pricing and cost determination for various
  pharmaceuticals.
- **Full-Stack Integration**: Demonstrated programmatic database access using JDBC to interface between a Java web
  application and the SQL backend.
- **SQL Optimization**: Wrote optimized queries to handle complex transactions between patients, doctors, and multiple
  pharmacy locations.

The project demonstrates a deep understanding of relational database design, normalization, and the practical application of SQL in a healthcare context. Relational integrity and normalization are the foundations of building reliable, scalable systems for sensitive healthcare data.

### Project Deliverables

<div style="text-align:center">
<iframe
    src="/assets/docs/Lab 19 Web App JDBC.pdf"
    width="90%"
    height="500px">
    This browser does not support PDFs. Please download the PDF to view it:
    <a href="/assets/docs/Lab 19 Web App JDBC.pdf">Download PDF</a>.
</iframe>
</div>

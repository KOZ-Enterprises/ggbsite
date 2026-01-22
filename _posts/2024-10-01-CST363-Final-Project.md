---
layout: post
tags: [ "cst363", 'csumb']
title: "Pharmacy Database System"
description: "A relational database design for managing patient prescriptions, medical providers, and pharmacy inventories."
project-title: "Pharmacy Database"
project-url: "/assets/docs/Lab 19 Web App JDBC.pdf"
image: "/assets/imgs/project/database.png"
---

This [database project](/assets/docs/Lab 19 Web App JDBC.pdf) focuses on the design and implementation of a relational
system tailored for pharmacy operations. It supports the tracking of patient health records, medication distribution,
and financial costs. This project includes:

<!--more-->

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

The project demonstrates a deep understanding of relational database design, normalization, and the practical
application of SQL in a healthcare context.

<div style="text-align:center">
<iframe
    src="/assets/docs/Lab 19 Web App JDBC.pdf"
    width="90%"
    height="500px">
    This browser does not support PDFs. Please download the PDF to view it:
    <a href="/assets/docs/Lab 19 Web App JDBC.pdf">Download PDF</a>.
</iframe>
</div>
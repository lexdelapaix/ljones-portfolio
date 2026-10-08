# Leslie A. Jones

## Cybersecurity | Cloud Security | Security Engineering

I am a cybersecurity professional and enterprise operations leader building toward cloud security and security engineering roles.

My technical work focuses on **AWS, Linux, security operations, security telemetry, vulnerability analysis, Python, and enterprise systems**. My portfolio demonstrates hands-on work building security environments, analyzing telemetry, investigating threats, and documenting security findings.

### Current Technical Focus

* ☁️ **Cloud Security:** AWS, EC2, IAM, VPC, cloud architecture
* 🛡️ **Security Operations:** OpenSearch, Suricata, threat detection, investigation
* 🐍 **Automation & Development:** Python, SQL, Bash, Flask, JSON
* 🐧 **Systems:** Linux, Ubuntu, Kali Linux, Windows
* 🔐 **Security Engineering:** Logging, telemetry pipelines, vulnerability analysis, authentication, access control
* 🏗️ **Infrastructure:** Docker; currently developing Terraform and infrastructure-as-code skills

---

# Featured Project

## [Jones International Bank SOC](./jones-international-bank-soc/)

**Cloud-hosted security analytics and threat detection platform built on AWS EC2.**

This project simulates an end-to-end SOC environment rather than simply consuming pre-existing alerts. I designed and configured the environment to generate, collect, ingest, analyze, and investigate security telemetry.

### Architecture

```text
Users / Simulated Attack Activity
              │
              ▼
     Flask Fintech Application
              │
              ▼
      Structured Security Logs
              │
              ▼
      Python Ingestion Pipeline
              │
              ▼
       OpenSearch Indexes
              │
       ┌──────┴──────┐
       ▼             ▼
 Application      Suricata
   Telemetry      Telemetry
       │             │
       └──────┬──────┘
              ▼
     Detection & Analysis
              │
              ▼
      SOC Dashboards
              │
              ▼
        Investigation
```

### Technologies

**AWS EC2 · Linux · OpenSearch · Python · Flask · Suricata · Docker · JSON · SQLite**

### What I Built

* Configured an AWS EC2/Linux environment for the security analytics platform.
* Built a Flask-based financial application with authentication, MFA, administrative functionality, transaction workflows, and fraud-review functionality.
* Implemented structured security logging for application activity.
* Developed Python-based ingestion workflows to parse, normalize, and load telemetry into OpenSearch.
* Integrated authorized PISCES security telemetry into custom OpenSearch indexes.
* Created dashboards for investigating authentication activity, reconnaissance, scanning, exploit activity, command-and-control indicators, and other security events.
* Documented an end-to-end workflow from activity generation through logging, ingestion, detection, analysis, and investigation.

### Security Investigation Scenarios

The environment supports investigation of activity including:

* Authentication anomalies
* SQL injection
* Cross-site scripting
* Log4Shell / RCE attempts
* SSH brute force
* Reconnaissance
* Vulnerability scanning
* Suspicious DNS activity
* Command-and-control indicators

**[View the full project →](./jones-international-bank-soc/)**

---

# Security Analysis

## Vulnerability Assessment Portfolio

My vulnerability analysis work focuses on identifying technical weaknesses, understanding exploitation paths, assessing impact, and documenting remediation recommendations in controlled academic and training environments.

### SUID Path Hijacking — Privilege Escalation

Analysis of improper privilege management in a SUID-root binary caused by unsafe PATH handling.

**Focus:** Linux security · privilege escalation · secure coding · remediation

**[View analysis →](./vulnerability-analysis/)**

### JWT Security Misconfiguration — Authentication Bypass

Analysis of weak JWT signing configuration that allowed token manipulation and privilege escalation.

**Focus:** authentication · authorization · web security · secure key management

### Cleartext Credential Transmission — Network Traffic Analysis

Analysis of sensitive credentials transmitted without adequate transport-layer protection.

**Focus:** network security · traffic analysis · TLS · secure authentication

---

# Security Operations Experience

My security operations work includes investigation of network, DNS, authentication, web application, and exploit-related activity using **OpenSearch and Suricata**.

Investigation experience includes:

* Log4Shell / RCE activity
* SQL injection
* XSS
* SSH brute force
* Vulnerability scanning
* Suspicious DNS
* Phishing
* Reconnaissance
* Authentication anomalies

A key focus of my analysis is distinguishing malicious activity from **legitimate or authorized behavior** by correlating multiple telemetry sources and validating environmental context before escalation.

---

# Enterprise Technology Experience

Before transitioning into cybersecurity, I developed extensive experience operating technology-enabled enterprise environments.

My professional background includes:

* Enterprise access and role management
* Segregation-of-duties controls
* Data validation and reconciliation
* System implementation and workflow redesign
* Technical troubleshooting and escalation
* Workforce technology supporting 5,000+ employees
* Operational technology and device management
* Technical training and change management

This experience informs my approach to security engineering: systems must be technically sound, operationally sustainable, documented, and usable by the people responsible for them.

---

# Education & Certifications

**B.S. Cybersecurity** — Bellevue College
GPA: 3.8 · Phi Theta Kappa · 2026

**A.A.S. Information Technology** — Bellevue College
GPA: 4.0 · 2024

### Certifications

* AWS Certified Solutions Architect – Associate
* CompTIA Security+
* AWS Certified Cloud Practitioner

---

# Connect

**LinkedIn:** [linkedin.com/in/lexdelapaix](https://www.linkedin.com/in/lexdelapaix)

**GitHub:** [github.com/lexdelapaix](https://github.com/lexdelapaix)

> All security work shown in this portfolio was completed in controlled academic, laboratory, or authorized training environments. Sensitive information, credentials, IP addresses, and system identifiers have been sanitized or omitted.

# VyomAI / KrishiSetu

# AI + Blockchain Powered Agricultural Claim Validation & Governance System

Transparent • Explainable • Multi-Authority • Decentralized

---
<img width="1915" height="1040" alt="Screenshot 2026-05-18 214756" src="https://github.com/user-attachments/assets/dd265dea-12c0-4062-ada6-f11e0282ce61" />
---

# Problem Statement

Traditional agricultural insurance systems often suffer from:

- delayed claim approvals
- lack of transparency
- centralized validation workflows
- poor auditability
- inefficient authority coordination
- fraud vulnerability
- limited explainability for farmers

Farmers frequently do not understand:
- why claims were rejected,
- which authority validated them,
- or what environmental evidence was used.

This creates distrust, delays, and operational inefficiencies across agricultural insurance ecosystems.

---

# Our Solution

VyomAI introduces an AI + Blockchain powered agricultural governance platform where:

- AI generates explainable environmental evidence,
- authorities collaboratively validate claims,
- governance policies dynamically control escalation logic,
- audit systems maintain transparency,
- and farmers can track claims in real time.

The system combines:

- AI-driven environmental analysis
- Explainable AI (XAI)
- Blockchain-backed validation workflows
- Multi-authority governance systems
- Transparent audit trails
- Decentralized approval mechanisms

---

# ⚠️ Important Setup Notice

This repository contains multiple enterprise-scale modules with heavy dependencies.

Some modules require:

- Docker Desktop
- Hyperledger Fabric
- Python ML environments
- Node.js ecosystem setup
- blockchain tooling
- WSL/Linux compatibility (recommended)

Modules can be executed independently depending on the use case.

---

# Demo & Documentation

## Demo Video
https://youtu.be/ULHjK2VhnNU

---

## Presentation
https://drive.google.com/file/d/1a_JqzKH1jlCRI1aKwrHNpNB3pTk0G_VO/view?usp=drive_link

---

# Workflow Overview

```text
1. Farmer submits claim
        ↓
2. AI Engine analyzes environmental conditions
        ↓
3. Risk score & confidence generated
        ↓
4. Insurance authority reviews evidence
        ↓
5. High-risk claims escalate to additional authorities
        ↓
6. Governance policies determine approval structure
        ↓
7. Approved claims move to payout systems
        ↓
8. Audit trail stored transparently
```

---

# System Architecture

```text
Frontend Layer
    ↓
Backend APIs
    ↓
AI Evidence Engine
    ↓
Blockchain Validation Layer
    ↓
Governance & Audit Infrastructure
    ↓
Banking & Payout Layer
```

---

# Core Components

# 🌾 Farmer Portal

The Farmer Portal enables transparent agricultural claim management.

Farmers can:
- submit claims,
- track approval stages,
- monitor validation timelines,
- understand AI-generated evidence explanations,
- and view authority endorsements in real time.

### Features

- multilingual support
- explainable AI decisions
- real-time validation tracking
- claim lifecycle transparency
- environmental evidence summaries

---

# 🤖 AI Evidence Generation Engine

The AI Engine acts as the analytical core of the platform.

The system analyzes:

- NDVI vegetation data
- rainfall trends
- soil moisture indicators
- environmental anomalies
- agricultural risk conditions

The engine generates:

- risk scores
- confidence scores
- explainable evidence summaries
- environmental intelligence reports

### Explainability Features

Instead of black-box outputs, the system explains:
- why a claim was flagged,
- which environmental factors contributed,
- and how the risk score was generated.


---

# 🏛 Multi-Authority Governance System

VyomAI introduces decentralized validation workflows where multiple authorities participate in claim governance.

Depending on risk classification:

```text
Low Risk       → Insurance Authority
Moderate Risk  → Insurance + State Authority
High Risk      → Multi-authority Escalation
```

Authorities can:
- approve claims,
- reject suspicious claims,
- escalate validations,
- and vote on governance policies.

### Governance Features

- decentralized approval workflows
- policy proposal system
- authority voting mechanisms
- dynamic risk thresholds
- transparent validation hierarchy


---

# 🏦 Banking & Payout Infrastructure

The Banking Module handles financial execution workflows for approved claims.

### Features

- payout queue management
- disbursement tracking
- claim-linked payout workflows
- financial transparency monitoring

### Screenshot

---

# 🔍 Audit & Transparency Layer

The Audit System maintains complete validation transparency across the insurance ecosystem.

Auditors can:
- inspect validation history,
- review authority endorsements,
- monitor governance actions,
- and verify claim approval trails.

### Transparency Features

- immutable validation records
- endorsement tracking
- governance traceability
- decision transparency

---

# Tech Stack

## Frontend
- React
- TypeScript
- Tailwind CSS

## Backend
- Node.js
- Express.js

## AI / ML
- Python
- pandas
- scikit-learn
- XGBoost

## Blockchain
- Hyperledger Fabric
- Docker Desktop

---

# Repository Structure

```text
KrishiSetu/
├── frontend/
├── backend/
├── ai_engine/
├── blockchain/
├── assets/
├── docs/
```

---

# Setup Instructions

# Clone Repository

```bash
git clone https://github.com/Karma-is-here/krishiSetu.git
```

---

# Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

# Backend Setup

```bash
cd backend
npm install
npm run dev
```

---

# AI Engine Setup

```bash
cd ai_engine
pip install -r requirements.txt
python app.py
```

---

# Blockchain Setup

⚠️ Docker Desktop must be running before starting blockchain services.

```bash
cd blockchain
./network.sh up
```

Additional Hyperledger configuration may be required depending on local environment setup.

---

# Research & Innovation Highlights

- Explainable AI-driven agricultural insurance
- Blockchain-backed governance workflows
- Multi-authority validation ecosystem
- Environmental evidence intelligence
- Transparent audit infrastructure
- Decentralized policy governance

---

# Prototype Note

This repository represents a research + hackathon prototype implementation.

Some modules may require:
- environment-specific setup,
- blockchain tooling configuration,
- dependency management,
- or dataset preprocessing.

Modules can also be executed independently.

---

# Future Scope

Potential future improvements include:

- real-time satellite API integration
- federated learning pipelines
- GIS-based risk visualization
- smart contract automation
- mobile farmer applications
- fraud anomaly detection

---

# Team

VyomAI / KrishiSetu Team

Developed for:
- AI + Blockchain Research
- Agricultural Governance Innovation
- Transparent Insurance Ecosystems
- Explainable Decision Infrastructure
- Hackathon / Research Prototype Development

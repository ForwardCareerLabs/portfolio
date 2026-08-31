# Cybersecurity, GRC & Operational Resilience Portfolio

Practical security work products showing how I turn ambiguous requirements into structured risk decisions, evidence-backed responses, and usable operational plans.

This portfolio is intentionally **artifact-first**. Rather than listing frameworks and buzzwords, it shows the reasoning, documentation discipline, and repeatable methods behind governance, risk, compliance, incident response, and resilience work.

> **Portfolio note:** These are demonstration artifacts built from fictional scenarios. They do not represent confidential client information, certifications, or unsupported claims of implemented controls.

## Core capabilities demonstrated

| Capability | What is demonstrated |
| --- | --- |
| Governance, Risk & Compliance | Risk statements, 5x5 scoring, treatment decisions, ownership, validation status |
| Third-Party / Security Reviews | Questionnaire drafting, evidence mapping, gap identification, claim validation |
| Incident Response | Ransomware tabletop design, decision points, injects, evaluation, improvement planning |
| Operational Resilience | Business impact thinking, downtime operations, dependencies, recovery priorities |
| Security Documentation | Clear language for technical and nontechnical reviewers without overstating evidence |
| Automation | Transparent Python risk-scoring logic with validation and automated tests |

## Featured work

### 1. [Control Evidence Mapping Case Study](evidence-mapping-case-study.md)
Takes a fictional healthcare technology security review from questionnaire language to evidence requirements, ownership, validation status, and defensible external wording. It demonstrates the difference between a policy statement and evidence that a control actually operates.

### 2. [Risk Register Case Study](risk-register-case-study.md)
Demonstrates likelihood and impact scoring, risk statements, control context, treatment direction, ownership, and evidence needs.

**Executable companion:** [`tools/risk_scoring.py`](tools/risk_scoring.py) implements a transparent 5x5 scoring model. [`tools/test_risk_scoring.py`](tools/test_risk_scoring.py) tests rating boundaries, score calculation, and invalid input handling.

Run it with:

```bash
cd tools
python risk_scoring.py
python -m unittest test_risk_scoring.py
```

### 3. [Security Questionnaire With Evidence Validation](security-questionnaire.md)
Shows how to draft responses without inventing controls. Proposed answers are separated from evidence requirements and validation status so uncertainty remains visible until an accountable owner verifies the claim.

### 4. [Ransomware Incident Response Tabletop](incident-response-tabletop.md)
A healthcare-oriented operational disruption exercise with objectives, escalating injects, expected actions, evaluator observations, and improvement-plan outputs.

### 5. [Security Documentation Before and After](before-after-security.md)
Shows how vague security language can be converted into clearer, scoped, reviewable statements.

## How I approach GRC work

1. **Define the claim.** Determine exactly what is being asserted or requested.
2. **Find the evidence.** Identify the policy, configuration, logs, test results, tickets, diagrams, or accountable owner that can support it.
3. **Expose uncertainty.** Mark gaps, assumptions, stale evidence, and scope limitations instead of hiding them behind polished language.
4. **Assess risk.** Translate technical conditions into likelihood, impact, operational consequence, and treatment decisions.
5. **Assign accountability.** Identify owners and concrete next actions.
6. **Make the output reviewable.** Another analyst should be able to understand how the conclusion was reached and challenge it if necessary.

## Design principles

- Never fabricate security or compliance evidence.
- Avoid absolute claims unless scope and evidence support them.
- Distinguish policy intent from technical implementation.
- Treat unknowns as findings to resolve, not blanks to fill creatively.
- Keep scoring logic transparent enough to explain to stakeholders.
- Connect security findings to operational and business consequences.
- Prefer reusable processes over one-off paperwork.

## Additional work

The related private **FSL Operator** project applies these principles to reusable workflows for risk scoring, security questionnaire drafting, tabletop exercise development, opportunity prioritization, pricing, and consulting operations. This public repository intentionally exposes methodology and sanitized artifacts without publishing internal business logic or confidential information.

## Background

My work sits at the intersection of cybersecurity, operational risk, emergency response, and healthcare operations. That perspective shapes these artifacts: security controls matter because systems support real operations, and documentation is useful only when it helps people make better decisions under normal conditions and during disruption.

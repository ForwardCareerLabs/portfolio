# Security Questionnaire With Evidence Validation

Security questionnaires are dangerous when the goal becomes simply producing a confident-looking answer. A defensible response should distinguish what is known, what evidence supports it, and what still requires validation.

The examples below use fictional organizational facts to demonstrate that process.

## Question 1

**How do you protect sensitive data at rest and in transit?**

### Draft response
Sensitive data is protected using encryption controls appropriate to the system and data type. Data in transit is restricted to approved encrypted protocols. Encryption at rest is enabled for supported production data stores.

### Evidence required before approval
- Current encryption standard or policy
- Configuration evidence for production databases and storage
- TLS configuration or approved network standard
- System inventory identifying exceptions
- Control owner confirmation

### Validation status
**Pending validation.** Do not state that all sensitive data is encrypted until the system inventory and configuration evidence support that claim.

---

## Question 2

**How do you manage user access?**

### Draft response
Access is provisioned according to business need and assigned roles. Access changes and removals follow an established lifecycle process, with privileged access receiving additional review.

### Evidence required before approval
- Access control policy
- Joiner, mover, leaver procedure
- Recent access review records
- Privileged access inventory
- Sample provisioning and termination tickets

### Validation status
**Partially supported.** The wording should be narrowed if periodic access-review evidence is unavailable.

---

## Question 3

**Do you have an incident response process?**

### Draft response
The organization maintains an incident response process covering identification, escalation, containment, investigation, recovery, communication, and post-incident review.

### Evidence required before approval
- Current incident response plan
- Defined severity or escalation criteria
- Incident roles and contact information
- Recent exercise, test, or incident record
- After-action documentation or lessons learned

### Validation status
**Pending evidence review.** A written plan alone does not prove the process is operationally tested.

---

## Question 4

**How do you monitor systems for security events?**

### Draft response
Selected systems generate security-relevant logs that are reviewed through centralized monitoring and alerting processes. Alerts are triaged according to defined procedures and escalated when investigation is required.

### Evidence required before approval
- Logging and monitoring standard
- SIEM or monitoring architecture
- Sample alert and investigation workflow
- Log-source inventory
- Retention configuration

### Validation status
**Scope must be confirmed.** Avoid claiming that all systems are centrally monitored unless coverage evidence supports it.

---

## Review method

For each questionnaire response:

1. Identify the exact claim being requested.
2. Gather the policy, technical, procedural, and operational evidence that supports it.
3. Confirm the scope of the control.
4. Narrow the response when exceptions or unknowns exist.
5. Assign an accountable reviewer or control owner.
6. Approve the final answer only after the evidence matches the wording.

This approach reduces the risk of creating unsupported compliance claims simply because a questionnaire expects a yes-or-no answer.

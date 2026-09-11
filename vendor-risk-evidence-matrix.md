# Vendor Risk Evidence Matrix

## Scenario

A fictional healthcare organization is evaluating a cloud vendor that supports scheduling and operational coordination. The vendor has completed an initial questionnaire, but several responses require evidence before the organization can rely on them.

The matrix below demonstrates how to separate a proposed response from the evidence needed to support it.

## Evidence review

| Control area | Proposed vendor response | Evidence required | Current status | Owner follow up |
|---|---|---|---|---|
| Security governance | The vendor maintains documented security policies that are reviewed at least annually | Current policy index, approval dates, review history, and accountable policy owners | Pending validation | Vendor risk lead requests the current policy index and approval record |
| Access management | Access is assigned by role and removed when personnel leave or change responsibilities | Access control policy, joiner mover leaver procedure, sample termination ticket, privileged access inventory, and recent access review | Partially supported | IAM owner confirms review frequency and validates a completed review |
| Encryption | Sensitive data is encrypted in transit and at rest within the production environment | Data flow diagram, approved encryption standard, storage configuration, TLS configuration, key management procedure, and documented exceptions | Scope unclear | Technical owner identifies covered systems and any unsupported data stores |
| Vulnerability management | Vulnerabilities are identified, prioritized, and remediated according to defined timelines | Vulnerability management standard, scan coverage, recent scan summary, remediation SLA, exception process, and sample closed finding | Pending validation | Security owner confirms asset coverage and provides recent remediation evidence |
| Incident notification | The vendor will notify the customer of qualifying security incidents within the contractual timeframe | Contract language, incident definition, notification timeframe, escalation contacts, and communication procedure | Contract review required | Legal and vendor management compare the contract to operational requirements |
| Business continuity | Critical services can be recovered within agreed objectives | Business continuity plan, disaster recovery plan, stated RTO and RPO, recent recovery test results, unresolved findings, and customer dependencies | Evidence gap | Business owner and IT review whether internal downtime procedures cover the remaining exposure |
| Subprocessor oversight | Subprocessors are assessed and monitored according to vendor requirements | Current subprocessor list, due diligence procedure, monitoring records, contractual flow down requirements, and customer notification process | Pending validation | Privacy and vendor risk owners confirm scope and notification requirements |

## Decision rules

- A completed questionnaire is not evidence by itself.
- A policy demonstrates intent, but it does not prove that a control operates as described.
- Evidence must match the systems, locations, services, and time period covered by the response.
- Unsupported universal terms such as all, always, and fully should be narrowed.
- A control should remain pending when the vendor cannot provide sufficient evidence or an accountable owner cannot validate the response.
- Residual risk should not be reduced until treatment actions are completed and reviewed.

## Example disposition

The vendor may remain under review while evidence is gathered. The organization should not label the vendor approved or compliant based only on confident questionnaire language.

A defensible decision records:

1. The business service being evaluated
2. The control claim under review
3. The evidence received
4. The gaps or exceptions identified
5. The responsible reviewer
6. The treatment or acceptance decision
7. The date and basis for final approval

## Portfolio note

This example uses fictional facts and does not represent a client assessment, certification, or legal conclusion.

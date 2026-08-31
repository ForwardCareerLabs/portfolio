# Risk Register Case Study

## Scenario

A fictional healthcare organization relies on a third-party cloud platform for scheduling and operational coordination. The vendor supports critical workflows, but the organization has incomplete evidence regarding recovery testing, privileged-access review, and notification requirements for service disruptions.

The objective is to convert those concerns into reviewable risks rather than a vague statement that the vendor is "high risk."

## Scoring model

Likelihood and impact are each scored from 1 to 5.

**Inherent risk = likelihood × impact**

| Score | Rating |
|---|---|
| 1–4 | Low |
| 5–9 | Moderate |
| 10–16 | High |
| 17–25 | Critical |

## Example register

| ID | Risk statement | Likelihood | Impact | Score | Rating | Treatment | Owner | Evidence / next step |
|---|---|---:|---:|---:|---|---|---|---|
| R-01 | If the scheduling platform experiences a prolonged outage and tested recovery capability is insufficient, critical scheduling and coordination functions may be unavailable, causing operational disruption and delayed service delivery. | 3 | 5 | 15 | High | Mitigate | Business owner + IT | Obtain recovery objectives, latest DR test results, outage procedures, and internal downtime workflow |
| R-02 | If privileged vendor or administrative access is not periodically reviewed, excessive or unnecessary access may remain active and increase the likelihood or impact of unauthorized activity. | 3 | 4 | 12 | High | Mitigate | Security / IAM | Obtain privileged-access process, review frequency, sample review record, and termination procedure |
| R-03 | If contractual incident-notification requirements are unclear, the organization may receive delayed notice of a security or availability event and lose time needed for escalation, continuity, or regulatory assessment. | 2 | 4 | 8 | Moderate | Mitigate / Transfer | Vendor owner + Legal | Review contract language, notification SLA, escalation contacts, and breach/availability definitions |

## Why the wording matters

A useful risk statement connects four things:

1. **Condition or weakness** — what could be inadequate or fail.
2. **Threat or event** — what could happen.
3. **Asset or business process** — what is affected.
4. **Consequence** — why the organization should care.

"Vendor has poor disaster recovery" is not a strong risk statement. It assumes a conclusion and does not explain the business consequence.

## Treatment logic

### R-01: Service recovery
The immediate goal is not to demand a perfect vendor architecture. The organization first needs enough evidence to understand recovery capability and determine whether internal downtime procedures can cover the remaining exposure.

Possible actions:
- Validate vendor RTO and RPO commitments
- Review recent recovery-test results
- Document internal manual downtime procedures
- Define escalation and communication ownership
- Test the combined vendor and internal recovery process

### R-02: Privileged access
Treatment should focus on evidence that privileged access is limited, reviewed, and removed appropriately.

Possible actions:
- Obtain role and privilege definitions
- Confirm periodic review frequency
- Review a sample completed access review
- Validate offboarding and emergency-access procedures

### R-03: Notification requirements
This risk can often be reduced through clearer contractual and operational requirements.

Possible actions:
- Define notification timeframes
- Clarify what events trigger notification
- Identify primary and backup contacts
- Include availability as well as security incidents where operationally important

## Residual risk

Residual risk should be scored **after** treatment evidence exists. It should not be reduced simply because an action item was created.

For example, R-01 should not move from High to Moderate merely because the vendor promises to provide a disaster-recovery document. The organization should review the document, determine whether recovery capability is adequate, and test its own downtime process before changing the residual rating.

## Takeaway

A risk register is useful when it creates accountability and drives decisions. The score is only a prioritization tool. The stronger deliverable is the combination of a defensible risk statement, supporting evidence, accountable ownership, treatment actions, and a clear basis for residual-risk acceptance.

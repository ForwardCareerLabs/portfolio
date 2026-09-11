# Business Continuity Dependency Analysis

## Scenario

A fictional healthcare organization relies on a cloud based scheduling and coordination platform used by several departments. The purpose of this analysis is to identify what must continue during an outage, which dependencies could prevent continuity, and what evidence is needed before recovery assumptions can be accepted.

## Critical process summary

| Process | Maximum tolerable disruption | Target recovery time | Data tolerance | Minimum continuity method |
|---|---:|---:|---:|---|
| Urgent scheduling changes | 2 hours | 1 hour | 15 minutes | Approved phone tree and controlled offline tracking |
| Routine scheduling | 8 hours | 4 hours | 1 hour | Offline work queue with reconciliation procedure |
| Staff notifications | 1 hour | 30 minutes | Not applicable | Independent emergency notification channel |
| Management reporting | 24 hours | 12 hours | 4 hours | Manual summary from validated departmental records |

The example values are planning assumptions. Business owners must validate them before they become approved recovery requirements.

## Dependency map

| Dependency | Failure effect | Existing assumption | Validation needed |
|---|---|---|---|
| Vendor application | Staff cannot view or update schedules | Vendor recovery will meet the internal target | Contracted RTO and recent recovery test results |
| Identity provider | Users may be unable to authenticate even when the application is available | Identity service has independent resilience | Architecture, failover design, and test evidence |
| Internet connectivity | Facilities may lose access to the cloud service | Secondary connectivity is available | Circuit inventory, failover procedure, and test record |
| Corporate email | Staff may lose the primary coordination channel | Teams can switch to another method | Approved alternate channel and current contact list |
| Vendor support | Escalation may be delayed during a widespread event | Priority support is available at all times | Support terms, escalation contacts, and response targets |
| Local staffing | Manual procedures may require more staff than are available | Departments can sustain the workaround | Timed exercise using realistic workload and staffing |

## Downtime workflow

### Detection and declaration

- Confirm whether the disruption affects one user, one facility, or the shared service.
- Assign an incident lead and document the declaration time.
- Establish a common operating picture using a channel that does not depend on the affected platform.
- Notify business owners and the vendor through approved escalation paths.

### Continuity

- Activate the approved offline process for the affected functions.
- Record every manual transaction needed for later reconciliation.
- Prioritize urgent work using predefined business rules.
- Track staffing, backlog, safety, privacy, and communication problems created by the workaround.

### Recovery

- Confirm that the service is technically available.
- Validate identity, data integrity, interfaces, and critical transactions before broad restoration.
- Reconcile offline records using an assigned owner and documented sequence.
- Monitor for duplicated, missing, or conflicting transactions.
- Obtain business owner approval before declaring normal operations restored.

## Exercise injects

1. The cloud platform becomes unavailable during a period of high scheduling volume.
2. The vendor acknowledges the event but cannot provide a recovery estimate.
3. Corporate email becomes intermittent, limiting the normal coordination method.
4. One facility reports that its offline contact list is outdated.
5. The platform returns, but several transactions appear to be missing.
6. Leadership requests an estimated operational impact and restoration time.

## Evaluation questions

- Who has authority to declare the disruption and activate downtime procedures?
- Which function receives first recovery priority and why?
- Can staff access the offline process without the affected network?
- How long can the workaround support expected volume?
- Who owns vendor escalation and internal status updates?
- What evidence is required before users return to the restored platform?
- How will manual records be reconciled and approved?
- Which gaps require corrective actions, accountable owners, and deadlines?

## Improvement plan structure

| Finding | Corrective action | Owner | Priority | Evidence of completion |
|---|---|---|---|---|
| Recovery targets have not been approved by business owners | Conduct a business impact review and approve recovery requirements | Business continuity and process owners | High | Approved impact analysis |
| Alternate contacts depend on the unavailable platform | Maintain a controlled offline contact method | Operations | High | Tested offline contact list |
| Vendor recovery capability has not been validated | Review contractual targets and recent recovery test evidence | Vendor management and IT | High | Completed evidence review |
| Manual reconciliation ownership is unclear | Define the reconciliation procedure and accountable approver | Operations and application owner | Moderate | Approved and exercised procedure |

## Portfolio note

This example demonstrates continuity analysis and exercise design using fictional information. It does not claim that a specific organization has implemented or tested these controls.

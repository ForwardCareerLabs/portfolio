# Incident Response Tabletop Exercise

## Scenario

A fictional healthcare organization experiences a ransomware event that disrupts access to scheduling, shared files, and several internal systems during normal operations. The exercise is designed to test decision-making, communications, operational continuity, and recovery coordination rather than technical trivia.

## Exercise objectives

1. Validate initial incident recognition and escalation.
2. Test coordination between security, IT, operations, leadership, communications, and business owners.
3. Identify how critical functions continue when key systems are unavailable.
4. Test decision-making around containment, evidence preservation, third-party dependencies, and communications.
5. Identify recovery priorities and unresolved ownership gaps.

## Participants

Typical participants may include:

- Incident response lead
- IT infrastructure
- Security operations
- Business continuity / emergency management
- Executive leadership
- Legal / privacy
- Communications
- Clinical or operational leadership
- Vendor management

## Module 1: Detection and escalation

### Initial inject
At 08:10, multiple employees report that shared files are inaccessible. Several workstations display unusual errors, and the help desk sees a sudden increase in tickets. Monitoring also identifies abnormal authentication activity from an administrative account.

### Discussion questions

- What information is needed before declaring a security incident?
- Who has authority to activate the incident response process?
- Who needs to be notified immediately?
- What systems or accounts should be isolated first?
- How will the team preserve evidence while containment begins?
- What operational functions are already affected?

### Expected actions

- Establish incident command / coordination structure
- Assign an incident lead and decision authority
- Begin incident documentation
- Preserve available logs and evidence
- Disable or restrict compromised credentials when supported by evidence
- Identify affected systems and critical dependencies
- Activate appropriate downtime procedures

## Module 2: Operational disruption expands

### Inject
By 10:30, scheduling and shared-document systems are unavailable. The organization confirms that the affected environment supports multiple critical departments. A third-party vendor reports that its support team is investigating unusual activity but cannot yet provide a recovery estimate.

### Discussion questions

- Which business functions receive recovery priority?
- How are downtime procedures activated and communicated?
- Which processes can operate manually, and for how long?
- Who communicates with the vendor and tracks commitments?
- What criteria would trigger executive, legal, regulatory, insurer, or law-enforcement notification?
- How will staff distinguish verified instructions from rumors?

### Expected actions

- Prioritize critical services based on operational impact
- Establish a common operating picture
- Assign vendor communication ownership
- Define internal update cadence
- Confirm regulatory and contractual notification triggers
- Track manual-workaround risks and resource constraints

## Module 3: Recovery and external pressure

### Inject
The organization learns that some systems can be restored from backup, but restoration will take time and the integrity of several systems must be validated first. A local reporter contacts the communications office asking whether the organization has been hit by ransomware. Employees are also posting speculation on social media.

### Discussion questions

- Who authorizes system restoration?
- What validation is required before systems return to production?
- How are recovery priorities communicated to business leaders?
- Who approves external messaging?
- What information can be released before the investigation is complete?
- What conditions must be met before the incident is considered contained or closed?

### Expected actions

- Establish restoration criteria
- Validate backup integrity and affected credentials
- Coordinate technical recovery with operational priorities
- Produce approved internal and external communications
- Maintain evidence and decision records
- Define transition from response to recovery

## Evaluator observations

Evaluators should capture more than whether participants produced the "right" answer. Useful observations include:

- Unclear authority or ownership
- Missing contact information
- Conflicting escalation thresholds
- Dependency assumptions that were not documented
- Manual workflows that cannot sustain expected volume
- Vendor responsibilities that are not contractually clear
- Communication channels that depend on affected systems
- Recovery priorities that differ between IT and operations

## After-action outputs

The exercise should produce an improvement plan with accountable actions.

| Finding | Corrective action | Owner | Priority | Evidence of completion |
|---|---|---|---|---|
| Incident declaration authority is unclear | Define declaration and escalation authority in the incident response plan | Security leadership | High | Approved plan revision |
| Downtime contacts are stored only on the affected network | Maintain an approved offline contact method | Business continuity | High | Tested offline contact list |
| Vendor recovery obligations are unclear | Review contractual recovery and notification requirements | Vendor management / Legal | Moderate | Updated contract or documented acceptance |
| Recovery priority has not been validated with operations | Conduct business impact review and define restoration tiers | IT + Operations | High | Approved recovery-priority matrix |

## Exercise principle

A tabletop exercise should create evidence about how the organization would actually respond. The objective is not to demonstrate that participants can recite an incident response plan. It is to expose assumptions, ownership problems, dependencies, and decisions that become expensive during a real event.
